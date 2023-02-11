import view
import controller


def main():

    branch = controller.generate_branch()
    view.show_to_console(branch)


if __name__ == '__main__':
    main()
