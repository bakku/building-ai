def intermediate():
    p_bot = 0.05
    p_8_digits_bot = 0.8
    p_8_digits_human = 0.01

    p_8_digits = p_8_digits_bot * p_bot + p_8_digits_human * (1 - p_bot)

    p_bot_8_digits = (p_8_digits_bot * p_bot) / p_8_digits

    print("P(8-digits) = %f" % p_8_digits)
    print("P(bot | 8-digits) = %f" % p_bot_8_digits)


def bot8(p_bot, p_8_digits_bot, p_8_digits_human):
    p_8_digits = p_8_digits_bot * p_bot + p_8_digits_human * (1 - p_bot)

    return (p_8_digits_bot * p_bot) / p_8_digits


def advanced():
    pbot = 0.1
    p8_bot = 0.8
    p8_human = 0.05

    print("P(bot | 8-digits) = %f" % bot8(pbot, p8_bot, p8_human))


if __name__ == "__main__":
    print("INTERMEDIATE")
    print("------------------")
    intermediate()
    print("------------------")

    print()

    print("ADVANCED")
    print("------------------")
    advanced()
    print("------------------")
