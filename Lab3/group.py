class Group:
    def __init__(self, group_name, subjects_hours):
        self.group_name = group_name
        self.subjects_hours = subjects_hours

    def __str__(self):
        return f"Group(group_name={self.group_name}, subjects_hours={self.subjects_hours})"
