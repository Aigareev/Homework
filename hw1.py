def fun(language, number):
    """
    :param language: English, Chinese, Russian
    :param number: Number of times to print results
    :return: Write “Hello” or “Nihao” or “Privet” on the screen number times
    """

    greetings = {'English': 'Hello', 'Chinese': 'Nihao', 'Russian': 'Privet'}

    for _ in range(int(number)):
        print(greetings.get(language, 'The language is not supported!'))


if __name__ == "__main__":
    fun(language='Chinese', number=3)
    fun(language='Russian', number=2)
    fun(language='English', number=1)
