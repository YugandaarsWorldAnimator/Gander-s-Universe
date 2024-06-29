from database.models import Animation, Frame, Session

def create_animation(name, description, frames):
    session = Session()
    animation = Animation(name=name, description=description)
    for frame_content in frames:
        frame = Frame(content=frame_content, animation=animation)
        session.add(frame)
    session.commit()

def get_animation(name):
    session = Session()
    return session.query(Animation).filter_by(name=name).first()

# Example usage
if __name__ == '__main__':
    create_animation('Test Animation', 'A test animation', ['Frame 1', 'Frame 2'])
    animation = get_animation('Test Animation')
    print(f'Animation: {animation.name}, Description: {animation.description}')
    for frame in animation.frames:
        print(f'Frame ID: {frame.id}, Content: {frame.content}')