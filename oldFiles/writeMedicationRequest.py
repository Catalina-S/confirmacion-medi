import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para guardar el JSON en MongoDB
def save_medication_request_to_mongodb(medication_request_json, collection):
    try:
        # Convertir el JSON string a un diccionario de Python
        medication_request_data = json.loads(medication_request_json)

        # Insertar el documento en la colección de MongoDB
        result = collection.insert_one(medication_request_data)

        # Retornar el ID del documento insertado
        return result.inserted_id
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "SamplePatientService"
    collection_name = "medication_requests"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)

    # JSON string correspondiente al artefacto MedicationRequest de HL7 FHIR
    medication_request_json = '''
    {
      "resourceType": "MedicationRequest",
      "status": "active",
      "intent": "order",
      "medicationCodeableConcept": {
        "coding": [
          {
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
            "code": "1049630",
            "display": "Acetaminophen 500 MG Oral Tablet"
          }
        ],
        "text": "Acetaminophen 500mg Tablet"
      },
      "subject": {
        "reference": "Patient/123"
      },
      "authoredOn": "2024-04-22",
      "requester": {
        "reference": "Practitioner/456"
      },
      "dosageInstruction": [
        {
          "text": "Take 1 tablet every 8 hours as needed for pain."
        }
      ]
    }
    '''

    # Guardar el JSON en MongoDB
    inserted_id = save_medication_request_to_mongodb(medication_request_json, collection)

    if inserted_id:
        print(f"MedicationRequest guardado con ID: {inserted_id}")
    else:
        print("No se pudo guardar el MedicationRequest.")


