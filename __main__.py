from Morador import Morador

def main():
    try:
        m1 = Morador('fernando', '102', '41987410667')
        print(m1.__dict__)
    except ValueError as erro:
        print(erro)
if __name__ == '__main__':
    main()

