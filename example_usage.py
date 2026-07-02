from client import GiftWrapCalculatorClient
def main():
    c = GiftWrapCalculatorClient()
    print(c.calculate_gift_wrap("premium", "Happy Birthday Bruce!"))
if __name__ == '__main__':
    main()
