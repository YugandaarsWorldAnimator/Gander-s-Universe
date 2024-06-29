from models import Animation, Frame, init_db

def setup_database():
    session = init_db()()

    # Add initial data if necessary
    animation = Animation(name='Sample Animation', description='This is a sample animation.')
    frame1 = Frame(content='Frame 1 content', animation=animation)
    frame2 = Frame(content='Frame 2 content', animation=animation)

    session.add(animation)
    session.commit()

if __name__ == '__main__':
    setup_database()