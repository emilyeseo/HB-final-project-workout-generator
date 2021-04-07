"""CRUD OPERATIONS."""
from model import db, User, Exercise, Workout_plan_exercise, Workout_plan, connect_to_db
import crud

import jinja2 import StrictUndefined



def create_user(firstname,lastname,email,password):
    """Create and return a new user."""

    user = User(firstname = firstname,
                lastname = lastname,
                email=email,
                password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_exercise(exercise_name, main_muscle_group, type_of_exercise, difficulty, equipment, instructions, exercise_img1, exercise_img2, reps):
    """Create and return a exercise."""

    exercise = Exercise(exercise_name = exercise_name,
                        main_muscle_group = main_muscle_group,
                        type_of_exercise = type_of_exercise,
                        difficulty = difficulty,
                        equipment = equipment,
                        instructions = instructions,
                        exercise_img1 = exercise_img1,
                        exercise_img2 = exercise_img2,
                        reps = reps)

    db.session.add(exercise)
    db.session.commit()

    return exercise

def create_workout_plan(user_id):
    """Create and return a workout plan."""
    
    workout_plan = Workout_plan(user_id = user_id)
    
    db.session.add(workout_plan)
    db.session.commit()

    return workout_plan


def create_workout_plan_exercise(workout_plan_id, exercise_id):
    """Create and return a workout plan exercise."""
    
    workout_plan_exercise = Workout_plan_exercise(workout_plan_id = workout_plan_id,
                                                    exercise_id = exercise_id)
    
    db.session.add(workout_plan_exercise)
    db.session.commit()

    return workout_plan_exercise

if __name__ == '__main__':
    from server import app
    connect_to_db(app)