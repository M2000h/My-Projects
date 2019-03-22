using System;
using System.Threading;
namespace Beep
{
    class Program
    { 
        static void Main(string[] args)
        {
            Console.Beep(2500, 300);
            Console.Beep(3000, 500);
            Thread.Sleep(800);
            Console.Beep(2500, 300);
            Console.Beep(2000, 500);
            Thread.Sleep(700);
            Console.Beep(3500, 250);
            Console.Beep(3000, 250);
            Console.Beep(3500, 250);
            Console.Beep(3000, 250);
            Console.Beep(3500, 250);
            Console.Beep(4000, 500);
        }
    }
}
