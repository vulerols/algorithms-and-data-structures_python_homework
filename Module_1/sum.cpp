// Задача про сумму
// На стандартном потоке ввода задаётся последовательность целых чисел.
// Каждое число последовательности не меньше -200 000 000 и не больше 200 000 000.
// На стандартный поток вывода напечатайте сумму этих чисел.

#include <iostream>
#include <regex>
#include <string>
using namespace std;

int main()
{
	std::ios::sync_with_stdio(false);
	long long int sum = 0;

	string temp;
	smatch m;
	regex e("-?\\d+");

	while (!cin.eof()) {
	
		getline(cin, temp);
		while (regex_search(temp, m, e)) {
			for (auto x : m)
				sum += stoi(x);
			temp = m.suffix().str();
		}
	}
	cout << sum;
    return 0;
}