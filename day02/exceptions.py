import logging
import traceback

# Logging Configuration
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Custom Exception
class InvalidMarksError(Exception):
    pass



# Function

def check_marks(marks):


    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks should be between 0 and 100"
        )

    return f"Valid Marks: {marks}"



# Main Program
try:

    marks = 150

    result = check_marks(marks)

    print(result)

except InvalidMarksError as e:

    print("Custom Exception Caught")
    print("Error:", e)

  
    # Traceback
    print("\nTraceback Details...:\n")

    traceback.print_exc()

  
    # Logging
    logging.exception(
        "Exception occurred while validating marks"
    )