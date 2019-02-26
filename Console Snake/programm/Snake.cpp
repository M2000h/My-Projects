#include <iostream>
#include <conio.h>
#include <bitset>
#include "windows.h"

using namespace std;

HANDLE hOCol = GetStdHandle(STD_OUTPUT_HANDLE);
#define BOARD_SIZE 10

int start();
void stop(int ShakeLenght);
bool check();
void print(int ShakeLenght);
void gotoxy(int x, int y,int color, int letter);

POINT p[100], Cookie;
void main()
{
	system("title SNAKE");
	CONSOLE_FONT_INFOEX cfi;
	wcscpy_s(cfi.FaceName, L"consolas");
	srand(43);
	do 
	{
		stop(start());
	} while (check());
}

int start() {
	SetConsoleTextAttribute(hOCol, 249);
	system("cls");
	int  ShakeLenght = 3;
	int n = 100;
	//cout << "your speed (recomended 50): ";
	//cin >> n;
	//system("cls");
	p[0].x = 0;
	p[0].y = 0;
	Cookie.x = rand() % BOARD_SIZE;
	Cookie.y = rand() % BOARD_SIZE;
	int direction = 0,
		q = 0;
	for (;;)
	{
		if (_kbhit())
		{
			_getch();
			q = _getch();
			if (q != 72 && q != 80 && q != 77 && q != 75)
				q = direction;
		}
		//for (a = 0;a < 2;a++)
		//{
		if (Cookie.x == p[0].x && Cookie.y == p[0].y)
		{
			ShakeLenght++;
			Cookie.x = rand() % BOARD_SIZE;
			Cookie.y = rand() % BOARD_SIZE;
		}
		//}

		for (int a = ShakeLenght; a > 0; a--)
		{
			p[a].x = p[a - 1].x;
			p[a].y = p[a - 1].y;
		}
		//начало стрелок
		if (abs(q - direction) == 8 || abs(q - direction) == 2)
			q = direction;//chek1
		switch (q) {
		case 72://вниз
			p[0].y = p[0].y == 0 ? BOARD_SIZE - 1 : p[0].y - 1;
			break;
		case 80://вверх
			p[0].y = p[0].y == BOARD_SIZE - 1 ? 0 : p[0].y + 1;
			break;
		case 77://впрао
			p[0].x = p[0].x == BOARD_SIZE - 1 ? 0 : p[0].x + 1;
			break;
		case 75://влево
			p[0].x = p[0].x == 0 ? BOARD_SIZE - 1 : p[0].x - 1;
			break;
		}
		if (q == 72 || q == 80 || q == 77 || q == 75)
			direction = q;
		//конец стрелок
		
		for (int a = 1; a < ShakeLenght - 1 && ShakeLenght > 4; a++)
			if (p[0].x == p[a].x && p[0].y == p[a].y)
				return ShakeLenght;

		if (ShakeLenght < 20)
			n = 100 - ShakeLenght * 4;
		Sleep(n);
		print(ShakeLenght);
	}
}


bool check() {
	while (true)
	{
		while (!_kbhit());
		int q = _getch();
		switch (q)
		{
		case 8:
			return false;
		case 13:
			return true;
		}
	}
}


void stop(int ShakeLenght) {
	system("cls");
	SetConsoleTextAttribute(hOCol, 249);
	printf("END\nSCORE - %d\n", ShakeLenght);
	
	SetConsoleTextAttribute(hOCol, 250);
	printf("TO PLAY AGAIN - PRESS ENTER\n");

	SetConsoleTextAttribute(hOCol, 252);
	printf("TO EXIT - PRESS BACK");
}


void print(int ShakeLenght)
{
	gotoxy(2 * p[1].x, 2 * p[1].y, 250, 219); //переход тулвищав голову

	gotoxy(2 * p[ShakeLenght - 1].x, 2 * p[ShakeLenght - 1].y, 250, 0); //удаление жопы

	gotoxy(2 * Cookie.x, 2 * Cookie.y, 254, 15);//печеньак

	gotoxy(2 * p[0].x, 2 * p[0].y, 252, 1);//прихерачиваниеголовы

	gotoxy(2 * BOARD_SIZE, 2 * BOARD_SIZE, 250, 0);
}


void gotoxy(int x, int y,int color, int letter)
{
	SetConsoleTextAttribute(hOCol, color);
	COORD  coord = { x, y };
	SetConsoleCursorPosition(hOCol, coord);
	cout << (char)letter << (char)letter;

	COORD  coord1 = { x, y+1 };
	SetConsoleCursorPosition(hOCol, coord1);
	cout << (char)letter << (char)letter;
}
