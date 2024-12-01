## **Автор проекта:**

Косов Руслан

## **Название проекта:**

Эмулятор игр приставки Game Boy

## **Технологии:**

Проект содержит 3 основных класса: MainWidget, LoadWidget, SaveWidget. MainWidget является подклассом QMainWidget, а остальные два являются под классом QDialog. Основными элементами прокета являются QFileDialog, QButtonGroup, QPushButton, QSlider. QFileDialog нужен для загрузки файлов игр и обложек этих игор. QButtonGroup и QPushButton для кнопок двух типов: для кнопок с изображением обложек игр, которые запускают игру, а второй тип для кнопок управления, в которые входят кнопка главное меню, кнопка настройки, кнопка выключения. QSlider нужен, чтобы перелистовать игры на экране.

## **Структура БД:**

БД содержит две таблицы под названиями roms и covers. В roms есть 4 колонки:
1. id, номер игры
2. name, имя игры
3. path, путь игры в компьютере
4. state, показатель, который равен 1 или 0 в зависимости есть ли сохраниение

В covers есть два столбца:
1. id, повторяющий id игры
2. path, путь до файла с картинкой

Также имеется файл csv, в котором записываются id последних 4 запущенных игр, а сами эти игры будет отображать в секторе "Продолжить игру"#   P y B o y Q T 
 
 
