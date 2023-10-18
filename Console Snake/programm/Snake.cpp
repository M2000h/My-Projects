#include <iostream>
#include <conio.h>
#include <bitset>
#include <cstdlib>
#include <windows.h>

using namespace std;

HANDLE hOCol = GetStdHandle(STD_OUTPUT_HANDLE);

#define BOARD_SIZE 10

#define SNAKE_BODY_CHAR 219
#define SNAKE_HEAD_CHAR 43
#define COOKIE_CHAR 42
#define BACK_GROUND_CHAR 1

#define SNAKE_BODY_COLOR 250
#define SNAKE_HEAD_COLOR 196
#define COOKIE_COLOR 230
#define BACK_GROUND_COLOR 255

int start();

void stop(int SnakeLenght);

bool check();

void print(POINT *SnakeBody, POINT Cookie, int SnakeLenght);

void gotoxy(int x, int y, int color, int letter);

int main() {
    system("title SNAKE");
    CONSOLE_FONT_INFOEX cfi;
    wcscpy_s(cfi.FaceName, L"consolas");
    SetConsoleTextAttribute(hOCol, BACK_GROUND_COLOR);
    srand(43);
    do {
        stop(start());
    } while (check());
    return 0;
}

int start() {
    POINT SnakeBody[100], Cookie;

    system("cls");
    int SnakeLenght = 3;
    int n = 100;
//    cout << "your speed (recomended 50): ";
//    cin >> n;
    system("cls");
    SnakeBody[0].x = 0;
    SnakeBody[0].y = 0;
    Cookie.x = rand() % BOARD_SIZE;
    Cookie.y = rand() % BOARD_SIZE;
    int direction = 0, q = 0;
    while (true) {
        if (_kbhit()) {
            _getch();
            if (_kbhit()) {
                q = _getch();
                if (q != 72 && q != 80 && q != 77 && q != 75)
                    q = direction;
            }
        }


        if (Cookie.x == SnakeBody[0].x && Cookie.y == SnakeBody[0].y) {
            SnakeLenght++;
            Cookie.x = rand() % BOARD_SIZE;
            Cookie.y = rand() % BOARD_SIZE;
        }


        for (int a = SnakeLenght; a > 0; a--) {
            SnakeBody[a].x = SnakeBody[a - 1].x;
            SnakeBody[a].y = SnakeBody[a - 1].y;
        }
        //начало стрелок
        if (abs(q - direction) == 8 || abs(q - direction) == 2)
            q = direction;//chek1

        switch (q) {
            case 72://вниз
                SnakeBody[0].y = SnakeBody[0].y ? --SnakeBody[0].y : BOARD_SIZE - 1;
                break;
            case 80://вверх
                SnakeBody[0].y = SnakeBody[0].y == BOARD_SIZE - 1 ? 0 : ++SnakeBody[0].y;
                break;
            case 77://впрао
                SnakeBody[0].x = SnakeBody[0].x == BOARD_SIZE - 1 ? 0 : ++SnakeBody[0].x;
                break;
            case 75://влево
                SnakeBody[0].x = SnakeBody[0].x ? --SnakeBody[0].x : BOARD_SIZE - 1;
                break;
        }

        direction = q;
        //конец стрелок

        for (int a = 1; a < SnakeLenght - 1 && SnakeLenght > 4; a++)
            if (SnakeBody[0].x == SnakeBody[a].x && SnakeBody[0].y == SnakeBody[a].y)
                return SnakeLenght;

        if (SnakeLenght < 20)
            n = 100 - SnakeLenght * 4;

        Sleep(n);
        print(SnakeBody, Cookie, SnakeLenght);
    }
}

bool check() {
    while (true) {
        while (!_kbhit());
        int q = _getch();
        if (q == 8)
            return false;
        if (q == 13)
            return true;
    }
}


void stop(int SnakeLenght) {
    system("cls");
    SetConsoleTextAttribute(hOCol, 249);
    printf("END\nSCORE - %d\n", SnakeLenght);

    SetConsoleTextAttribute(hOCol, 250);
    printf("TO PLAY AGAIN - PRESS ENTER\n");

    SetConsoleTextAttribute(hOCol, 252);
    printf("TO EXIT - PRESS BACK");
}


void print(POINT *SnakeBody, POINT Cookie, int SnakeLenght) {
    gotoxy(SnakeBody[1].x, SnakeBody[1].y, SNAKE_BODY_COLOR, SNAKE_BODY_CHAR); //переход тулвищав голову

    gotoxy(SnakeBody[SnakeLenght - 1].x, SnakeBody[SnakeLenght - 1].y, BACK_GROUND_COLOR,
           BACK_GROUND_CHAR); //удаление жопы

    gotoxy(Cookie.x, Cookie.y, COOKIE_COLOR, COOKIE_CHAR);//печеньак

    gotoxy(SnakeBody[0].x, SnakeBody[0].y, SNAKE_HEAD_COLOR, SNAKE_HEAD_CHAR);//прихерачиваниеголовы

    gotoxy(BOARD_SIZE, BOARD_SIZE, BACK_GROUND_COLOR, BACK_GROUND_CHAR);
}


void gotoxy(int x, int y, int color, int letter) {
    SetConsoleTextAttribute(hOCol, color);
    SetConsoleCursorPosition(hOCol, {(short) (2 * x), (short) (2 * y)});
    cout << (char) letter << (char) letter;

    SetConsoleCursorPosition(hOCol, {(short) (2 * x), (short) (2 * y + 1)});
    cout << (char) letter << (char) letter;
}
