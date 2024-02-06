
class JobOffer:
    def __init__(self, title: str, responsibilities: str, requirements: str) -> None:
        self.title = title
        self.responsibilities = responsibilities
        self.requirements = requirements


class JobOffersPracuje(JobOffer):
    def __init__(self, title: str, responsibilities: str, requirements: str, technologies: str) -> None:
        super().__init__(title, responsibilities, requirements)
        self.technologies = technologies
