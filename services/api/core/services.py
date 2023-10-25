from datetime import datetime

def verify_active_allocations(instance) -> bool:
    for allocation in instance.allocations.all():
        if datetime.now().timestamp() < allocation.end_time.timestamp() and not allocation.deleted_at:
            return True
    return False