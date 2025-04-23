from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.patient import Patient
import json

collection = connect_to_mongodb("SamplePatientService", "medication_requests")

router = APIRouter()

@router.put("/medication-request/{medication_request_id}/confirm")
async def confirm_medication_request(medication_request_id: str):
    updated_result = medication_requests_collection.update_one(
        {"_id": ObjectId(medication_request_id)},
        {"$set": {"status": "confirmed"}}
    )
    if updated_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="MedicationRequest no encontrado")
    return {"message": "MedicationRequest confirmado exitosamente"}


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

def UpdateMedicationRequestStatus(req_id: str, new_status: str):
    try:
        med_req = collection.find_one({"_id": ObjectId(req_id)})
        if not med_req:
            return "notFound", None

        result = collection.update_one(
            {"_id": ObjectId(req_id)}, 
            {"$set": {"status": new_status}}
        )

        if result.matched_count > 0:
            med_req["_id"] = str(med_req["_id"])
            return "success", med_req
        else:
            return "errorUpdating", None
    except Exception as e:
        return str(e), None


