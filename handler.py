from app import main


def run(event, context):
    results = main.init()
    print(results)


if __name__ == "__main__":
    run('', '')
