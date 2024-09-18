import tomllib
from pydantic import BaseModel, Field
from pathlib import Path


class USER_input(BaseModel):
    Variable: str = Field(default="tas")
    Project: str = Field(default="cmip5")
    Product: str = Field(default="cmip")
    Experiment: str = Field(default="historical")
    Institute: str = Field(default="gerics")
    Model: str = Field(default="mpi-esm-hr2")


def load_user_input_from_file(file_path: Path) -> USER_input:

    with file_path.open("rb") as f:
        data = tomllib.load(f)
    return USER_input(**data)


file_path = Path("input_data.toml")

user_input = load_user_input_from_file(file_path)


print(user_input)
