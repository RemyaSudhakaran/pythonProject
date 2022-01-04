def OuterFn():
    print("Outer Function Message")

    def InnerFn():
        print("Inner Function Message")

    InnerFn()


OuterFn()
