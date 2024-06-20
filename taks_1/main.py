from pymongo import MongoClient, errors

client = MongoClient("mongodb+srv://dmytronaumenkods:K2Znw7KnmTA64Av@clustermain.zifz1la.mongodb.net/Cats?retryWrites=true&w=majority&appName=ClusterMain")

db = client.Cats


cats = [
        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"]
        },
        {
            "name": "murzik",
            "age": 5,
            "features": ["чорний", "грайливий", "не любить собак"]
        },
        {
            "name": "vaska",
            "age": 4,
            "features": ["білий", "любит гладитись", "спить на ліжку"]
        },
        {
            "name": "pushok",
            "age": 2,
            "features": ["пухнастий", "сірий", "дуже гучний"]
        },
        {
            "name": "simba",
            "age": 1,
            "features": ["рудий", "дуже активний", "любит гратись"]
        },
        {
            "name": "leopold",
            "age": 6,
            "features": ["старий", "мудрий", "повільний"]
        }
    ]

# result_one = db.Cats.insert_many(cats)

#CRUD realization

def read_all_cats():
    return [cat for cat in db.Cats.find()]


def read_cat_by_name(name):
    return db.Cats.find_one({"name":name})


def update_cat_name(name, new_age):
    result = db.Cats.update_one({"name":name},{"$set":{"age":new_age}})
    return result

def update_cat_feature(name, new_feature):
    result = db.Cats.update_one({"name":name},{"$addToSet":{"features":new_feature}})
    return result


def delete_cat_by_name(name):
    result = db.Cats.delete_one({"name":name})
    return result


def delete_all_cats():
    result = db.Cats.delete_many({})
    return result


if __name__ == "__main__":
    # print(read_all_cats())
    print(read_cat_by_name("simba"))
    print(update_cat_name("pushok", 3))
    print(update_cat_feature("pushok", "стал старым"))
    print(delete_cat_by_name("pushok"))
    print(delete_all_cats())