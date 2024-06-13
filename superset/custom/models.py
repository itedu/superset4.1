from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Enum,
    exists,
    ForeignKey,
    Integer,
    orm,
    String,
    Table,
    Text,
)
from sqlalchemy.orm import relationship, sessionmaker
from superset.models.helpers import AuditMixinNullable

Session = sessionmaker()


class Custom(Model, AuditMixinNullable):
    __tablename__ = "ab_user_custom"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    address = Column(String(1000))

    @classmethod
    def get_tenant_id(self):
        try:
            return self.tenant_id
        except Exception:
            return None
