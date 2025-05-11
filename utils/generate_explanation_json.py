import json

explanation_text = """A Django ForeignKey defines a many-to-one relationship. For example, many 'Note' objects can be related to one 'User'. In this setup, the Note model will have a ForeignKey pointing to User. Django automatically creates a reverse relationship from User to Note, accessible via the 'related_name' if provided (e.g., user.notes.all()). This is useful when you want to associate multiple objects (like Notes or Profiles) with a single owner (like a User)."""  # noqa E501

data = {"explanation": explanation_text}

# Write to a file
with open("foreignkey_explanation.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
