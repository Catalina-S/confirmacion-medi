from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.patient import Patient
import json

collection = connect_to_mongodb("SamplePatientService", "medication_requests")



def WriteMedicationRequest(data: dict):
    try:
        result = collection.insert_one(data)
        return "success", str(result.inserted_id)
    except Exception as e:
        return str(e), None

def GetMedicationRequestById(req_id: str):
    try:
        med_req = collection.find_one({"_id": ObjectId(req_id)})
        if not med_req:
            return "notFound", None
        med_req["_id"] = str(med_req["_id"])
        return "success", med_req
    except Exception as e:
        return str(e), None
