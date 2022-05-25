{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/temazinkin/Anonymizer/blob/master/lesson%201.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "ynvmfW8SX7vr"
      },
      "source": [
        "# Простейшие задачи ЕГЭ на код"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "MW45swfFX7vs"
      },
      "source": [
        "## Номер 6"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "apmZREuDX7vs"
      },
      "source": [
        "Определите, при каком наименьшем введённом значении переменной s программа выведет число 128. Для вашего удобства программа представлена на четырёх языках программирования.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "n = 4\n",
        "while s < 37:\n",
        "    s = s + 3\n",
        "    n = n * 2\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "RL5xx9xyX7vs",
        "outputId": "fb6a279d-0fd0-4b3d-d66b-63d6cc1b15bc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "22\n"
          ]
        }
      ],
      "source": [
        "for t in range(100):\n",
        "    s = t\n",
        "    n = 4\n",
        "    while s < 37:\n",
        "        s = s + 3\n",
        "        n = n * 2\n",
        "    if n == 128:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "split",
        "id": "6veJTZIEX7vs",
        "outputId": "08af3299-7228-4cb1-a803-b5778070592b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "22\n",
            "128\n"
          ]
        }
      ],
      "source": [
        "s = int(input())\n",
        "n = 4\n",
        "while s < 37:\n",
        "    s = s + 3\n",
        "    n = n * 2\n",
        "print(n)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "OQiqTh0aX7vt"
      },
      "source": [
        "Определите, при каком наибольшем введённом значении переменной s программа выведет число 64. Для вашего удобства программа представлена на четырёх языках программирования.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "n = 1\n",
        "while s < 47:\n",
        "    s = s + 4\n",
        "    n = n * 2\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "daqxgz2rX7vt"
      },
      "source": [
        "Какое максимальное значение переменной&nbsp;s, подаваемое на&nbsp;вход программе, для которого в&nbsp;результате работы программы на&nbsp;экран будет выведено значение&nbsp;64?\n",
        "\n",
        "```\n",
        "n = 1024\n",
        "s = int(input())\n",
        "while s >= 5:\n",
        "    s = s - 5\n",
        "    n = n // 2\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "center",
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "sLA8iMHIX7vt",
        "outputId": "7268b52f-3ba4-4728-f68d-b72328bf3cda"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "26\n"
          ]
        }
      ],
      "source": [
        "for t in range(1000, -1, -1):\n",
        "    s = t\n",
        "    n = 1\n",
        "    while s < 47:\n",
        "        s = s + 4\n",
        "        n = n * 2\n",
        "    if n == 64:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "center",
        "id": "e2v3aWsVX7vu",
        "outputId": "2dcab22e-464d-4274-f725-6802469d1404"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "20\n",
            "21\n",
            "22\n",
            "23\n",
            "24\n"
          ]
        }
      ],
      "source": [
        "for t in range(1000):\n",
        "    n = 1024\n",
        "    s = t\n",
        "    while s >= 5:\n",
        "        s = s - 5\n",
        "        n = n // 2\n",
        "    if n == 64:\n",
        "        print(t)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "W-sZHvzwX7vu"
      },
      "source": [
        "Определите, при каком наименьшем введённом значении переменной s программа выведет число 60. Для вашего удобства программа представлена на четырёх языках программирования.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "n = 36\n",
        "while s < 2020:\n",
        "    s = s * 2\n",
        "    n = n + 3\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "r-Cqt8YIX7vu",
        "outputId": "044862a6-c578-4b53-bc58-4a77b7e8f433"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "8\n"
          ]
        }
      ],
      "source": [
        "for t in range(1, 100):\n",
        "    s = t\n",
        "    n = 36\n",
        "    while s < 2020:\n",
        "        s = s * 2\n",
        "        n = n + 3\n",
        "    if n == 60:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "n58ZIq-pX7vv"
      },
      "source": [
        "Определите, при каком наименьшем введённом значении переменной s программа выведет число 66.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "s = (s + 1) // 7\n",
        "n = 36\n",
        "while s < 2050:\n",
        "    s = s * 2\n",
        "    n = n + 3\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "i4I80npiX7vv",
        "outputId": "405d837f-684f-4c14-aa9e-ef4502f4a6c7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "20\n"
          ]
        }
      ],
      "source": [
        "for t in range(6, 100):\n",
        "    s = t\n",
        "    s = (s + 1) // 7\n",
        "    n = 36\n",
        "    while s < 2050:\n",
        "        s = s * 2\n",
        "        n = n + 3\n",
        "    if n == 66:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "tAbS-iO4X7vv"
      },
      "source": [
        "Определите, при каком наименьшем введённом значении переменной s программа выведет число 128.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "s = 3 * (s // 10)\n",
        "n = 1\n",
        "while s < 221:\n",
        "    s = s + 13\n",
        "    n = n * 2\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NUcmYAJ8X7vw",
        "outputId": "ba9778c4-c980-4674-ce20-dac82c9736df"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "440\n"
          ]
        }
      ],
      "source": [
        "for t in range(1000):\n",
        "    s = t\n",
        "    s = 3 * (s // 10)\n",
        "    n = 1\n",
        "    while s < 221:\n",
        "        s = s + 13\n",
        "        n = n * 2\n",
        "    if n == 128:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "tNln8-n_X7vw"
      },
      "source": [
        "Определите, сколько существует различных целых значений переменной s, при вводе которых данная программа выведет число 256. Для вашего удобства программа представлена на четырёх языках программирования.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "s = 3 * (s // 10)\n",
        "n = 1\n",
        "while s < 221:\n",
        "    s = s + 13\n",
        "    n = n * 2\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fkAfosQHX7vx",
        "outputId": "8b30da23-bfcc-4ffa-c5ba-3eb81f23aceb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "50\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for t in range(10000):\n",
        "    s = t\n",
        "    s = 3 * (s // 10)\n",
        "    n = 1\n",
        "    while s < 221:\n",
        "        s = s + 13\n",
        "        n = n * 2\n",
        "    if n == 256:\n",
        "        count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "Vo28DaYoX7vx"
      },
      "source": [
        "Известно, что при вводе некоторых положительных значений переменных s и x данная программа выводит число 17. Определите, при каком наименьшем введённом значении переменной x это возможно. Для вашего удобства программа представлена на четырёх языках программирования.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "x = int(input())\n",
        "s = 100 * s + x\n",
        "n = 1\n",
        "while s < 2021:\n",
        "    s = s + 5 * n\n",
        "    n = n + 1\n",
        "print(n)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "-64qamLTX7vy",
        "outputId": "fa1d75a3-56bc-46dc-f572-76255d1e3527"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1\n"
          ]
        },
        {
          "ename": "NameError",
          "evalue": "name 'stop' is not defined",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31mNameError\u001b[0m\u001b[0;31m:\u001b[0m name 'stop' is not defined\n"
          ]
        }
      ],
      "source": [
        "for tx in range(1, 100):\n",
        "    for ts in range(1, 100):\n",
        "        s = ts\n",
        "        x = tx\n",
        "        s = 100 * s + x\n",
        "        n = 1\n",
        "        while s < 2021:\n",
        "            s = s + 5 * n\n",
        "            n = n + 1\n",
        "        if n == 17:\n",
        "            print(tx)\n",
        "            stop"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "YdrjSP7dX7vy"
      },
      "source": [
        "## Номер 22"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "xjIAE8FyX7vy"
      },
      "source": [
        "Ниже на пяти языках записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа a и b. Укажите наименьшее из таких чисел x, при вводе которого алгоритм печатает сначала 2, а потом 13.\n",
        "\n",
        "```\n",
        "x = int(input())\n",
        "a, b = 0, 0\n",
        "while x > 0:\n",
        "    a = a + 1\n",
        "    b = b + x % 100\n",
        "    x = x // 100\n",
        "print(a)\n",
        "print(b)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "rwXbe9nOX7vz",
        "outputId": "a811b2fc-a198-4963-a286-5a62d48829c4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "112\n"
          ]
        }
      ],
      "source": [
        "for t in range(100000):\n",
        "    x = t\n",
        "    a, b = 0, 0\n",
        "    while x > 0:\n",
        "        a = a + 1\n",
        "        b = b + x % 100\n",
        "        x = x // 100\n",
        "    if a == 2 and b == 13:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "wbuzRoKdX7vz"
      },
      "source": [
        "Ниже на пяти языках программирования записан алгоритм. Получив на вход натуральное число x, этот алгоритм печатает число S. Укажите такое наименьшее число x, при вводе которого алгоритм печатает пятизначное число.\n",
        "\n",
        "```\n",
        "x = int(input())\n",
        " S = x; \n",
        " R = 0\n",
        " while x > 0:\n",
        "    d = x % 2\n",
        "    R = 10 * R + d\n",
        "    x = x / / 2\n",
        " S = R + S\n",
        " print(S)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "ou5N68hKX7vz",
        "outputId": "93543aeb-b023-4687-f542-cb6474bf90f7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10018\n",
            "17\n"
          ]
        }
      ],
      "source": [
        "for t in range(100):\n",
        "    x = t\n",
        "    S = x\n",
        "    R = 0\n",
        "    while x > 0:\n",
        "        d = x % 2\n",
        "        R = 10 * R + d\n",
        "        x = x // 2\n",
        "    S = R + S\n",
        "    if 10_000 <= S <= 99_999:\n",
        "        print(S)\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "6HY7KQd_X7vz"
      },
      "source": [
        "Ниже на пяти языках программирования записан алгоритм. Получив на вход число N, этот алгоритм печатает число q. Укажите наименьшее из таких чисел N, при вводе которых алгоритм напечатает 17.\n",
        "\n",
        "```\n",
        "q = 0\n",
        "n = int(input())\n",
        "for i in range(1, n):\n",
        "    if n % i == 0:\n",
        "        q = i\n",
        "print(q)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "4IR4U_XyX7v0",
        "outputId": "595a0ab9-432b-483a-e997-aecb9334e081"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "34\n"
          ]
        }
      ],
      "source": [
        "for t in range(100):\n",
        "    q = 0\n",
        "    n = t\n",
        "    for i in range(1, n):\n",
        "        if n % i == 0:\n",
        "            q = i\n",
        "    if q == 17:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "6NAQ9pmyX7v0"
      },
      "source": [
        "Ниже на пяти языках программирования записан алгоритм. Получив на вход число x, этот алгоритм печатает число M. Известно, что x > 100. Укажите наименьшее такое (т. е. большее 100) число x, при вводе которого алгоритм печатает 60.\n",
        "\n",
        "```\n",
        "x = int(input())\n",
        " L = x-30\n",
        " M = x+30\n",
        "while L != M:\n",
        "    if L > M:\n",
        "        L = L - M\n",
        "    else:\n",
        "        M = M - L\n",
        "print(M)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "pg9mb1mGX7v0",
        "outputId": "2ee5c3bd-94ef-4d27-a5bf-c65953050663"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "150\n"
          ]
        }
      ],
      "source": [
        "for t in range(101, 1000):\n",
        "    x = t\n",
        "    L = x-30\n",
        "    M = x+30\n",
        "    while L != M:\n",
        "        if L > M:\n",
        "            L = L - M\n",
        "        else:\n",
        "            M = M - L\n",
        "    if M == 60:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "0wrlmqPUX7v1"
      },
      "source": [
        "Ниже на&nbsp;пяти языках программирования записан алгоритм. Получив на&nbsp;вход число&nbsp;x, этот алгоритм печатает числа: a&nbsp;и&nbsp;b. Укажите наибольшее четырехзначное число&nbsp;x, при вводе которого алгоритм печатает сначала&nbsp;5, а&nbsp;потом&nbsp;7.\n",
        "```\n",
        "a = 10\n",
        "b = 0\n",
        "x = int(input())\n",
        "while x > 0:\n",
        "    y = x % 10\n",
        "    x = x // 10\n",
        "    if y < a:\n",
        "        a = y\n",
        "    if y > b:\n",
        "        b = y\n",
        "print(a)\n",
        "print(b)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "51VWaYnNX7v1"
      },
      "outputs": [],
      "source": [
        "for t in range(1000, 9999+1): # range(a, b) a ≤ N < b\n",
        "    "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "7BXFIZHPX7v1"
      },
      "source": [
        "Ниже записан алгоритм. После выполнения алгоритма было напечатано 3 числа. Первые два напечатанных числа — это числа 7 и 42. Какое наибольшее число может быть напечатано третьим?\n",
        "```\n",
        "x = int(input())\n",
        "y = int(input())\n",
        "if y > x:\n",
        "    z = x\n",
        "    x = y\n",
        "    y = z\n",
        "a = x\n",
        "b = y\n",
        "while b > 0:\n",
        "    r = a % b\n",
        "    a = b\n",
        "    b = r\n",
        "print(a)\n",
        "print(x)\n",
        "print(y)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "hoO6dqBzX7v1",
        "outputId": "905d4689-b357-4021-8ec2-c580c3041c66"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "35\n"
          ]
        }
      ],
      "source": [
        "maxY = 0\n",
        "for tx in range(1000):\n",
        "    for ty in range(1000):\n",
        "        x = tx\n",
        "        y = ty\n",
        "        if y > x:\n",
        "            z = x\n",
        "            x = y\n",
        "            y = z\n",
        "        a = x\n",
        "        b = y\n",
        "        while b > 0:\n",
        "            r = a % b\n",
        "            a = b\n",
        "            b = r\n",
        "        if a == 7 and x == 42:\n",
        "            maxY = max(maxY, y)\n",
        "print(maxY)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "iawtOSbNX7v4"
      },
      "source": [
        "Ниже записана программа. Получив на вход число s, эта программа печатает два числа. При каком наименьшем значении s после выполнения программы на экран будет выведено сначала число 10, затем 19.\n",
        "\n",
        "```\n",
        "s = int(input())\n",
        "P = 10\n",
        "Q = 8\n",
        "K1 = 0\n",
        "K2 = 0\n",
        "while s <= 100:\n",
        "    s = s + P\n",
        "    K1 = K1 + 1\n",
        "\n",
        "while s >= Q:\n",
        "    s = s - Q\n",
        "    K2 = K2 + 1\n",
        "K1 += s\n",
        "K2 += s\n",
        "\n",
        "print(K1, K2)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_style": "split",
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "aJziiqxgX7v4",
        "outputId": "568df706-7f92-4812-f4bd-aed29374a2ac"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "70\n"
          ]
        }
      ],
      "source": [
        "for t in range(100):\n",
        "    s = t\n",
        "    P = 10\n",
        "    Q = 8\n",
        "    K1 = 0\n",
        "    K2 = 0\n",
        "    while s <= 100:\n",
        "        s = s + P\n",
        "        K1 = K1 + 1\n",
        "\n",
        "    while s >= Q:\n",
        "        s = s - Q\n",
        "        K2 = K2 + 1\n",
        "    K1 += s\n",
        "    K2 += s\n",
        "\n",
        "    if K1 == 10 and K2 == 19:\n",
        "        print(t)\n",
        "        break"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "hUYVpqckX7v5"
      },
      "source": [
        "## Номер 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "66XgBx1rX7v5"
      },
      "source": [
        "Логическая функция F задаётся выражением `(x ∨ y) → (z ≡ x)`.  \n",
        "Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F. Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.\n",
        "\n",
        "| Переменная 1 | Переменная 2 | Переменная 3 | Функция |\n",
        "|:------------:|:------------:|:------------:|:-------:|\n",
        "|      ???     |      ???     |      ???     |    F    |\n",
        "|              |       0      |       0      |    0    |\n",
        "|              | 0            |              | 0       |"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "mQsTrFJxX7v5",
        "outputId": "26f72072-5505-40e6-b7fc-447ce125d00c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "x y z F\n",
            "1 0 0 0\n",
            "1 1 0 0\n"
          ]
        }
      ],
      "source": [
        "print('x y z F')\n",
        "for x in 0,1:\n",
        "    for y in 0,1:\n",
        "        for z in 0,1:\n",
        "            F = int((x or y) <= (z == x))\n",
        "            if F == 0 and x+y+z <= 1:\n",
        "                print(x, y, z, F)\n",
        "            elif F == 0 and y+z <= 1:\n",
        "                print(x, y, z, F)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "GGZIFc8CX7v5"
      },
      "source": [
        "Логическая функция F задаётся выражением `(x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w`. На рисунке приведён фрагмент таблицы истинности функции F, содержащий все наборы аргументов, при которых функция F ложна. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных w, x, y, z. Все строки в представленном фрагменте разные.\n",
        "\n",
        "| Перем.1 | Перем.2 | Перем.3 | Перем.4 |\n",
        "|:-------:|:-------:|:-------:|:-------:|\n",
        "| ???     | ???     | ???     | ???     |\n",
        "|         | 0       |         |         |\n",
        "| 1       | 0       |         | 0       |\n",
        "| 1       |         | 0       | 0       |"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "C9loWvl1X7v5",
        "outputId": "fac940b4-7f78-41dc-bc34-1369c14aa271"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "x y z w\n",
            "0 0 1 1\n",
            "0 1 0 1\n",
            "1 1 0 1\n"
          ]
        }
      ],
      "source": [
        "print('x y z w')\n",
        "for x in 0,1:\n",
        "    for y in 0,1:\n",
        "        for z in 0,1:\n",
        "            for w in 0,1:\n",
        "                F = int((x and (not y)) or (y == z) or (not w))\n",
        "                if F == 0:\n",
        "                    print(x, y, z, w)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "LNnKBjOpX7v6"
      },
      "source": [
        "Логическая функция F задаётся выражением `((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x))`. Дан&nbsp;частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F. Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.\n",
        "\n",
        "| Переменная 1 | Переменная 2 | Переменная 3 | Переменная 4 | Функция |\n",
        "|:------------:|:------------:|:------------:|:------------:|:-------:|\n",
        "|      ???     |      ???     |      ???     |      ???     |    F    |\n",
        "|       1      |       0      |       1      |       1      |    1    |\n",
        "|       1      |       0      |              |       0      |    1    |\n",
        "|       1      |       0      |              |       0      |    1    |"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "RWnEKEwXX7v6"
      },
      "source": [
        "Логическая функция F задаётся выражением `(w → x) ∧ ((y → z) ≡ (x → y))`. На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.\n",
        "\n",
        "| Переменная 1 | Переменная 2 | Переменная 3 | Переменная 4 | Функция |\n",
        "|:------------:|:------------:|:------------:|:------------:|:-------:|\n",
        "|       0      |       1      |       1      |       0      |    1    |\n",
        "|       1      |              |              |       0      |    1    |\n",
        "|              |       1      |       0      |              |    1    |"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "q-2B9ZVhX7v6",
        "outputId": "27814a0e-8f88-409e-e1c2-73684db4eef8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "x y z w F\n",
            "0 0 1 0 1 3\n",
            "0 1 1 0 1 1\n",
            "1 1 1 0 1 2\n"
          ]
        }
      ],
      "source": [
        "print('x y z w F')\n",
        "for x in 0,1:\n",
        "    for y in 0,1:\n",
        "        for z in 0,1:\n",
        "            for w in 0,1:\n",
        "                F = int((w <= x) and ((y <= z) == (x <= y)))\n",
        "                if F == 1 and x+y+z+w == 2:\n",
        "                    print(x, y, z, w, F, 1)\n",
        "                elif F == 1 and x+w == 1:\n",
        "                    print(x, y, z, w, F, 2)\n",
        "                elif F == 1 and y+z == 1:\n",
        "                    print(x, y, z, w, F, 3)\n",
        "                        "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "IblybQw6X7v7"
      },
      "source": [
        "## Номер 8"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "rEBtT5aZX7v7"
      },
      "source": [
        "Некоторый алфавит содержит три различные буквы. Сколько четырёхбуквенных слов можно составить из букв данного алфавита (буквы в слове могут повторяться)?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "Ev2qlgFNX7v7",
        "outputId": "ccb5d04e-2ea7-420a-c422-27d9a0111340"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "81\n"
          ]
        }
      ],
      "source": [
        "print(3*3*3*3)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "NQ7z0A3gX7v8"
      },
      "source": [
        "Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О? Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "QQDGPohrX7v8",
        "outputId": "07ac098b-d96e-435e-8dea-760136d1b6bd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "150\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in \"МТР\":\n",
        "    for l2 in \"МЕТРО\":\n",
        "        for l3 in \"МЕТРО\":\n",
        "            for l4 in \"ЕО\":\n",
        "                word = l1+l2+l3+l4\n",
        "                count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "RTyxPohgX7v9"
      },
      "source": [
        "Иван составляет 5-буквенные коды из букв И, В, А, Н. Буквы в коде могут повторяться, использовать все буквы не обязательно, но букву И нужно использовать хотя бы один раз. Сколько различных кодов может составить Иван?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "WvdqRny0X7v9",
        "outputId": "611d02b4-e5b9-4525-ecad-0566c44366bf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "781\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in \"ИВАН\":\n",
        "    for l2 in \"ИВАН\":\n",
        "        for l3 in \"ИВАН\":\n",
        "            for l4 in \"ИВАН\":\n",
        "                for l5 in \"ИВАН\":\n",
        "                    word = l1+l2+l3+l4+l5\n",
        "                    if word.count('И') >= 1:\n",
        "                        count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "BpiAG3hnX7v9"
      },
      "source": [
        "Николай составляет 4-буквенные коды из букв Н, И, К, О, Л, А, Й. Каждую букву можно использовать любое количество раз, при этом код не может начинаться с буквы Й и должен содержать хотя бы одну гласную. Сколько различных кодов может составить Николай?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "-QuxROWfX7v9",
        "outputId": "a9ced019-1a7b-4cd6-b15e-29a3a4db5fd0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1866\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in 'НИКОЛА':\n",
        "    for l2 in 'НИКОЛАЙ':\n",
        "        for l3 in 'НИКОЛАЙ':\n",
        "            for l4 in 'НИКОЛАЙ':\n",
        "                word = l1+l2+l3+l4\n",
        "                if word.count('И') + word.count('А') + word.count('О') >= 1:\n",
        "                    count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "fUnbA-tSX7v9"
      },
      "source": [
        "Вася составляет 6-буквенные слова, в которых могут быть использованы только буквы В, И, Ш, Н, Я, причём буква В используется не более одного раза. Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем. Слово не должно начинаться с буквы Ш и оканчиваться гласными буквами. Словом считается любая допустимая последовательность букв, не обязательно осмысленная. Сколько существует таких слов, которые может написать Вася?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XEfHUKzRX7v-",
        "outputId": "6e0f3ef0-f8b6-4ad9-97e7-2812f25990ca"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4352\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in 'ВИНЯ':\n",
        "    for l2 in 'ВИШНЯ':\n",
        "        for l3 in 'ВИШНЯ':\n",
        "            for l4 in 'ВИШНЯ':\n",
        "                for l5 in 'ВИШНЯ':\n",
        "                    for l6 in 'ВШН':\n",
        "                        word = l1+l2+l3+l4+l5+l6\n",
        "                        if word.count('В') <= 1:\n",
        "                            count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "CEl8GldzX7v-"
      },
      "source": [
        "Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А. Каждую букву нужно использовать ровно 1 раз, при&nbsp;этом Ь нельзя ставить первым и нельзя ставить после гласной. Сколько различных кодов может составить Ольга?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "xQ2FqpNXX7v-",
        "outputId": "57602671-4d5a-48ba-8fd5-e132a8340871"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "48\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in 'ОЛГА':\n",
        "    for l2 in 'ОЛЬГА':\n",
        "        for l3 in 'ОЛЬГА':\n",
        "            for l4 in 'ОЛЬГА':\n",
        "                for l5 in 'ОЛЬГА':\n",
        "                    word = l1+l2+l3+l4+l5\n",
        "                    if len(set(word)) == 5 and 'ОЬ' not in word and 'АЬ' not in word:\n",
        "                        count += 1\n",
        "print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "n1oPHxTKX7v_"
      },
      "source": [
        "Все 6-буквенные слова, составленные из букв А, О, У, записаны в обратном алфавитном порядке. Вот начало списка:\n",
        "```\n",
        "1. УУУУУУ\n",
        "2. УУУУУО\n",
        "3. УУУУУА\n",
        "4. УУУУОУ\n",
        "```\n",
        "На каком месте от начала списка находится слово ОУУУОО."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "NjnNo3bxX7v_",
        "outputId": "3e5b75cb-8203-4f57-aee7-e3ea2a5b864d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "248\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in reversed(sorted('АОУ')):\n",
        "    for l2 in reversed(sorted('АОУ')):\n",
        "        for l3 in reversed(sorted('АОУ')):\n",
        "            for l4 in reversed(sorted('АОУ')):\n",
        "                for l5 in reversed(sorted('АОУ')):\n",
        "                    for l6 in reversed(sorted('АОУ')):\n",
        "                        word = l1+l2+l3+l4+l5+l6\n",
        "                        count += 1\n",
        "                        if word == 'ОУУУОО':\n",
        "                            print(count)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "UqySCkafX7wA"
      },
      "source": [
        "Все трёхбуквенные слова, составленные из букв П, А, Р, У, С, записаны в алфавитном порядке и пронумерованы, начиная с 1. Начало списка выглядит так:\n",
        "```\n",
        "1. ААА\n",
        "2. ААП\n",
        "3. ААР\n",
        "4. ААС\n",
        "5. ААУ\n",
        "6. АПА\n",
        "```\n",
        "Под каким номером в списке идёт первое слово, которое начинается с буквы С?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "RCLs6KhlX7wA",
        "outputId": "9426c210-db41-40de-cda9-83b93bbe5914"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "76\n"
          ]
        },
        {
          "ename": "NameError",
          "evalue": "name 'stop' is not defined",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31mNameError\u001b[0m\u001b[0;31m:\u001b[0m name 'stop' is not defined\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in sorted('ПАРУС'):\n",
        "    for l2 in sorted('ПАРУС'):\n",
        "        for l3 in sorted('ПАРУС'):\n",
        "            word = l1+l2+l3\n",
        "            count += 1\n",
        "            if l1 == 'С':\n",
        "                print(count)\n",
        "                stop"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "pycharm": {
          "name": "#%% md\n"
        },
        "id": "QeY-VSB4X7wB"
      },
      "source": [
        "Валерия составляет 3-буквенные коды из букв В, А, Л, Е, Р, И, Я, причём буква В должна входить в код ровно один раз. Все полученные коды Валерия записала в алфавитном порядке и пронумеровала. Начало списка выглядит так:\n",
        "```\n",
        "1. ААВ\n",
        "2. АВА\n",
        "3. АВЕ\n",
        "```\n",
        "На каком месте будет записан первый код, не содержащий ни одной буквы А?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "pycharm": {
          "name": "#%%\n"
        },
        "id": "tuLSaUuKX7wB",
        "outputId": "b18dae5d-819e-4d61-dfdf-495700f095ed"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "ВЕЕ\n",
            "20\n"
          ]
        },
        {
          "ename": "NameError",
          "evalue": "name 'stop' is not defined",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31mNameError\u001b[0m\u001b[0;31m:\u001b[0m name 'stop' is not defined\n"
          ]
        }
      ],
      "source": [
        "count = 0\n",
        "for l1 in sorted('ВАЛЕРИЯ'):\n",
        "    for l2 in sorted('ВАЛЕРИЯ'):\n",
        "        for l3 in sorted('ВАЛЕРИЯ'):\n",
        "            word = l1+l2+l3\n",
        "            if word.count('В') == 1:\n",
        "                count += 1\n",
        "                if word.count('А') == 0:\n",
        "                    print(word)\n",
        "                    print(count)\n",
        "                    stop"
      ]
    }
  ],
  "metadata": {
    "celltoolbar": "Необработанный формат ячейки",
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.4"
    },
    "latex_envs": {
      "LaTeX_envs_menu_present": false,
      "autoclose": false,
      "autocomplete": true,
      "bibliofile": "biblio.bib",
      "cite_by": "apalike",
      "current_citInitial": 1,
      "eqLabelWithNumbers": false,
      "eqNumInitial": 1,
      "hotkeys": {
        "equation": "Ctrl-E",
        "itemize": "Ctrl-I"
      },
      "labels_anchors": false,
      "latex_user_defs": false,
      "report_style_numbering": false,
      "user_envs_cfg": false
    },
    "colab": {
      "name": "Урок 1.ipynb",
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}