phonebook = {
    "06201112233": { "name" : "Robert", "address": "Budapest", "email": "robert@gmail.com"},
    "06202223344": { "name" : "Csaba", "address": "Pécs", "email": "csaba@gmail.com"},
    "06203334455": { "name" : "Kriszta", "address": "Eger", "email": "kriszta@gmail.com"}
}

del phonebook["06203334455"]
print(phonebook)