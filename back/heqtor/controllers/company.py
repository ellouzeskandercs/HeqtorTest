from heqtor.core import Session
from heqtor.models import User, Company


def create_company(name: str, siren: str, email: str, phone: str, made_by_id: int):
    session = Session()
    try:
        creator = session.query(User).get(made_by_id)
        if creator is None:
            raise Exception("Company creator not found")
        company = Company(name=name, siren=siren, email=email, phone=phone)
        session.add(company)
        session.query(Company).filter(
            CompanyRestaurateur.siren == siren,
        ).one()  # update company instance with id from database
        creator.company_id = company.id
        session.commit()
        return company.get_small_data()
    except:
        session.rollback()
        return False
    finally:
        session.close()


# TODO
# get company by id, delete company
