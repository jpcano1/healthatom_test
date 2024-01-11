MANAGEMENT_DIR = src
PYTHON_INTERPRETER = python3
CURRENCY = usd

retrieve_currency:
	$(PYTHON_INTERPRETER) -m $(MANAGEMENT_DIR).main --currency $(CURRENCY)
