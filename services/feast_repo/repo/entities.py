from feast import Entity

# Entité principale : un utilisateur StreamFlow
user = Entity(
    name="user",
    join_keys=["user_id"],
    description="Utilisateur : Client StreamFlow",
)
