"""Module for PyDantic models."""
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, field_validator


class CurrencyUpdateCreate(BaseModel):
    """PyDantic model for currency update model."""

    model_config = ConfigDict(from_attributes=True)

    currency: str
    value: float
    updated_at: date


class ObsData(BaseModel):
    """PyDantic model for obs data model."""

    index_date_string: str = Field(..., alias="indexDateString")
    value: str
    status_code: str = Field(..., alias="statusCode")


class Series(BaseModel):
    """PyDantic model for Series data model."""

    description_eng: str = Field(..., alias="descripIng")
    description_esp: str = Field(..., alias="descripEsp")
    series_id: str = Field(..., alias="seriesId")
    obs_data: list[ObsData] = Field(..., alias="Obs")


class Response(BaseModel):
    """PyDantic model for response model."""

    code: int = Field(..., alias="Codigo")
    description: str = Field(..., alias="Descripcion")
    series: Series = Field(..., alias="Series")
    series_info: list = Field([], alias="seriesInfos")

    @field_validator("code")
    @classmethod
    def code_validator(cls, value: int) -> int:
        """Validate code field."""
        if value != 0:
            raise ValueError("Must be 0")
        return value
