#!/bin/bash -e
PROJECT_NAME=$(basename "$(git config --get remote.origin.url)" | sed 's/.git$//')
IMAGE_NAME=${IMAGE_NAME:-"healthatom_test"}
IMAGE_TAG=${DOCKER_IMAGE_TAG:-"dev"}
SRC_DIR="src"
VOLUME="$(pwd):/app"

# Variables for directory structure.
REPO_ROOT_DIR="$(git rev-parse --show-toplevel)"

# parse arguments.
cmd=$1
shift

case ${cmd} in
    h | help)
        # self-print to stdout.
        cat "$0" | less
        ;;

    b | build)
        # build Docker image.
        echo "Build Docker image: ${IMAGE_NAME}"
        docker build \
            --build-arg ENV="dev" \
            -t "${IMAGE_NAME}":"${IMAGE_TAG}" \
            -f "${REPO_ROOT_DIR}"/Dockerfile "${REPO_ROOT_DIR}"
        ;;

    l | linters)
        echo "Running linters on Docker image: ${DOCKER_IMAGE_NAME}"
        echo -e "\nChecking black format..."
        docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" "black --check --diff --color ${SRC_DIR} ${TESTS_DIR}"
        echo -e "\nRunning flake8..."
        docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" "flake8 ${SRC_DIR}"
        echo -e "\nRunning mypy..."
        docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" "mypy ${SRC_DIR}"
        echo -e "\nRunning isort..."
        docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" "isort ${SRC_DIR} ${TESTS_DIR} --check"
        echo -e "\nRunning PydocStyle..."
        docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" "pydocstyle ${SRC_DIR}"
        ;;

    t | tests)
        echo "Build Docker image: ${IMAGE_NAME}"
        if [[ -z "${TARGET_COV}" ]]; then
            echo "Running without coverage"
            docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" pytest --cov=./${SRC_DIR} ./${SRC_DIR}/tests
        else
            docker run -v "${VOLUME}" --rm "${IMAGE_NAME}":"${IMAGE_TAG}" pytest --cov=./${SRC_DIR} ./${SRC_DIR}/tests --cov-fail-under=${TARGET_COV}
        fi
        ;;

    *)
        echo "Bad command. Options are:"
        grep -E "^    . \| .*\)$" "$0"
        ;;
esac
