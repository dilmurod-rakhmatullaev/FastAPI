from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": "Something",
    "age": 12,
}

data_wo_age = {
    "email": "123@mail.com",
    "bio": "Something",
    #"gender": "male",
    #"birthday": "1980-01-01",
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "User added!"}

@app.get("/users")
def get_users() -> list[UserSchema]:
    return users



#class UserAgeSchema(UserSchema):
#    age: int = Field(ge=0, le=130)
    #description: str


user1 = UserSchema(**data_wo_age)
# user2 = UserAgeSchema(**data)

#print(repr(user1))
#print(repr(user2))
#print(repr(user3))