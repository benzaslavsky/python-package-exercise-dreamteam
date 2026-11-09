"""Demonstrate both public functions using made-up passwords."""

from password_roaster import roast_password, score_password


def main():
    samples = [
        "", "Password123!", "Go7!", "abcabcabcabc",
        "sillygoose7", "VelvetOtter7!", "VelvetOtter7!Moonrise",
    ]
    for number, password in enumerate(samples, start=1):
        print(f"Example {number}: {score_password(password)}/100")
        print(roast_password(password))
        print()


if __name__ == "__main__":
    main()
