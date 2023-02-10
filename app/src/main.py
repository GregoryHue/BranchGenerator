import view
import controller


def main():

    
    branch = controller.generate_branch()
    view.display_branch(branch)

if __name__ == '__main__':
    main()