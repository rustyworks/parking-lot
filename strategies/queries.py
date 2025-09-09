class SlotQuery:

    @classmethod
    def where(cls, slots: list[object], **conditions):
        filtered_slots = [slot for slot in slots if all(getattr(slot.car, k) == v for k, v in conditions.items())]
        return filtered_slots

    @classmethod
    def find(cls, slots: list[object], **conditions):
        result = cls.where(slots, **conditions)
        return result[0] if result else None
