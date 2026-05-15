from pydantic import (
    BaseModel,
    field_validator,
    model_validator,
    computed_field,
    Field,
    EmailStr
)

from typing import (
    List,
    Dict,
    Annotated,
    Literal,
    Optional
)


class Address(BaseModel):

    city: Annotated[
        str,
        Field(description="Enter the city")
    ]

    state: Annotated[
        str,
        Field(description="Enter the state")
    ]

    pincode: Annotated[
        int,
        Field(description="Enter the pincode")
    ]


class PatientCreate(BaseModel):

    id: Annotated[
        str,
        Field(
            ...,
            description="Patient ID",
            examples=["P001"]
        )
    ]

    name: str

    age: int = Field(gt=0)

    gender: Literal[
        "male",
        "female",
        "others"
    ]

    height: float = Field(gt=0)

    weight: float = Field(gt=0)

    email: EmailStr

    contact: Dict[str, str]

    allergies: List[str]

    address: Address

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        valid_domain = [
            "nichi.com",
            "ndr.com"
        ]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError(
                "Not a valid email domain"
            )

        return value

    @model_validator(mode="after")
    def validate_emergency_number(self):

        if (
            self.age > 70 and
            "emergency" not in self.contact
        ):
            raise ValueError(
                "Emergency number required"
            )

        return self

    @computed_field
    @property
    def bmi(self) -> float:

        return round(
            self.weight / (self.height ** 2),
            2
        )

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Under weight"

        elif self.bmi < 25:
            return "Normal"

        return "Obese"


class PatientUpdate(BaseModel):

    name: Optional[str] = None

    age: Optional[int] = Field(
        default=None,
        gt=0
    )

    gender: Optional[
        Literal[
            "male",
            "female",
            "others"
        ]
    ] = None

    height: Optional[float] = Field(
        default=None,
        gt=0
    )

    weight: Optional[float] = Field(
        default=None,
        gt=0
    )

    contact: Optional[
        Dict[str, str]
    ] = None

    allergies: Optional[
        List[str]
    ] = None

    address: Optional[
        Address
    ] = None