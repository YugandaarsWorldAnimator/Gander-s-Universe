from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Animation(Base):
    __tablename__ = 'animations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    frames = relationship('Frame', back_populates='animation')

class Frame(Base):
    __tablename__ = 'frames'
    id = Column(Integer, primary_key=True)
    animation_id = Column(Integer, ForeignKey('animations.id'))
    content = Column(String, nullable=False)
    animation = relationship('Animation', back_populates='frames')

# Initialize database connection
def init_db():
    engine = create_engine('sqlite:///animation_tool.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Create a session
Session = init_db()