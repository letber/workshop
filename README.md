# workshop
Завдання TODO-list 

Короткий опис завдання:
Ваше завдання реалізувати программу-трекер ваших планів (планер). Програма має зчитувати - що і до коли треба зробити. Всі “плани” вона має записувати у відповідну таблицю (завдання креативне - може бути не лише стовпці “Що” і “До коли” - але ці два обов’язково мають бути присутніми). При кожному запуску має перевіряти сьогоднішню дату і перевіряти які плани мають дедлайн до сьогодні - відповідно нагадувати про них. Додавання нових планів і видалення старих - якщо вже виконано - здійснюється через командну стрічку. Також необхідно реалізувати пріоритетність виконання планів - може бути таке - що на один день маєте кілька дедлайнів - вони між собою мають мати свою пріоритетність і згідно із цією пріоритетністю мають бути записані в csv-файл


# Що необхідно реалізувати?

* Взаємодію з користувачем з командною стрічки - робота команди триває доти - доки користувач не захоче закінчити роботу (опція “Вийти” має бути присутня обов’язково)
* Записування нових планів - якщо на день, коли це треба зробити вже є план - збуджувати питання пріоритетності і всім завданням дня надавати нову пріоритетність. Наприклад:
 > На день 21.12.21 маєте вже план: “Зробити домашнє завдання з матаналізу” 
 > З’явилось нове завдання - “Купити квиток на літак” і найкращий день, коли будуть акційні ціни - саме 21.12.21 - тому ви додаєте це завдання теж - на цьому моменті має відбуватись наступне: 
* Користувачу виводяться всі існуючі дедлайни на цей день - якщо він один, то йому одразу надається пріоритетність 1 
* В користувача запитується пріоритетність нового завдання - вона може бути або на 1 менше ніж найменший пріоритет, що вже є, або від 1 до найменшого - і тоді всі інші плани зсуваються відносно нового завдання по пріоритетності вниз
* Зчитування дати і перевірка всіх невиконаних завдань - їх виведення має бути посортоване по “дедлайнах” - від найближчого і далі
* Записування у csv-файл всіх завдань (завдання креативне - може бути не лише стовпці “Що” і “Дедлайн” - але ці два обов’язково мають бути присутніми)


# Вимоги виконання:

* Робота має бути розподілення на трьох людей - кожен працює із своєю частиною і заливає на гітхаб на свою гілку ! 
* Програма має працювати поки користувач не обере опцію “Вийти”
* Програма повинна зберігати наявні завдання у файл. Під час запуску програма повинна зчитати минулі завдання з файлу (якщо вони є), а під час вимкнення програма повинна зберегти поточні завдання у файл.
