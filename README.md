Горчаков Роман Владимирович. Вариант 2
# Лабораторная работа 4.7. Основы работы с Tkinter

Tkinter – это пакет для Python, предназначенный для работы с библиотекой Tk. Библиотека Tk содержит компоненты графического интерфейса пользователя (graphical user interface – GUI), написанные на языке программирования Tcl. Под графическим интерфейсом пользователя (GUI) подразумеваются все те окна, кнопки, текстовые поля для ввода, скроллеры, списки, радиокнопки, флажки и др., которые вы видите на экране, открывая то или иное приложение. Через них вы взаимодействуете с программой и управляете ею. Все эти элементы интерфейса будем называть виджетами (widgets).

Чтобы написать GUI-программу, надо выполнить приблизительно следующее:
1. Создать главное окно.
2. Создать виджеты и выполнить конфигурацию их свойств (опций).
3. Определить события, то есть то, на что будет реагировать программа.
4. Описать обработчики событий, то есть то, как будет реагировать программа.
5. Расположить виджеты в главном окне.
6. Запустить цикл обработки событий.

Первым аргументом в конструктор виджета передается виджет-хозяин, то есть тот, на котором будет располагаться создаваемый. В случае, когда элементы GUI помещаются непосредственно на главное окно, родителя можно не указывать. У функций, которые вызываются при наступлении события с помощью метода bind, должен быть один параметр. Обычно его называют event, то есть "событие".

В любом приложении виджеты не разбросаны по окну как попало, а организованы, интерфейс продуман до мелочей и обычно подчинен определенным стандартам. В Tkinter существует три способа конфигурирования свойств виджетов:
* в момент создания объекта,
* с помощью метода config , он же configure ,
* путем обращения к свойству как к элементу словаря.

Самыми важными свойствами виджета класса Button являются text , с помощью которого устанавливается надпись на кнопке, и command для установки действия, то есть того, что будет происходить при нажатии на кнопку. По умолчанию размер кнопки соответствует ширине и высоте текста, однако с помощью свойств width и height эти параметры можно изменить. Единицами измерения в данном случае являются знакоместа. Такие свойства как bg, fg, activebackground и activeforeground определяют соответственно цвет фона и текста, цвет фона и текста во время нажатия и установки курсора мыши над кнопкой.

Виджет Label просто отображает текст в окне и служит в основном для информационных целей (вывод сообщений, подпись других элементов интерфейса). Свойства метки во многом схожи с таковыми у кнопки. Однако у меток нет опции command . Поэтому связать их с событием можно только с помощью метода bind.

Текстовые поля предназначены для ввода информации пользователем. Однако нередко также для вывода, если предполагается, что текст из них будет скопирован. Текстовые поля как элементы графического интерфейса бывают однострочными и многострочными.

В Tkinter существует три так называемых менеджера геометрии – упаковщик, сетка и размещение по координатам. Упаковщик (packer) вызывается методом pack, который имеется у всех виджетов-объектов. Если к элементу интерфейса не применить какой-либо из менеджеров геометрии, то он не отобразится в окне. При этом в одном окне (или любом другом родительском виджете) нельзя комбинировать разные менеджеры. Если вы начали размещать виджеты методом pack , то не надо тут же использовать методы grid (сетка) и place (место).

В tkinter многострочное текстовое поле создается от класса Text. По умолчанию его размер равен 80-ти знакоместам по горизонтали и 24-м по вертикали. Если в текстовое поле вводится больше линий текста, чем его высота, то оно само будет прокручиваться вниз. При просмотре прокручивать вверх-вниз можно с помощью колеса мыши и стрелками на клавиатуре. Однако бывает удобнее пользоваться скроллером – полосой прокрутки. В tkinter скроллеры производятся от класса Scrollbar. Объект-скроллер связывают с виджетом, которому он требуется. Это не обязательно многострочное текстовое поле.

Особенностью текстового поля библиотеки Tk является возможность форматировать текст в нем, то есть придавать его разным частям разное оформление. Делается это с помощью методов tag_add и tag_config . Первый добавляет тег, при этом надо указать его произвольное имя и отрезок текста, к которому он будет применяться. Метод tag_config настраивает тегу стили оформления.

В Tkinter от класса Radiobutton создаются радиокнопки, от класса Checkbutton – флажки. Радиокнопки не создают по одной, а делают связанную группу, работающую по принципу переключателей. Когда включена одна, другие выключены. Экземпляры Checkbutton также могут быть визуально оформлены в группу, но каждый флажок независим от остальных. Каждый может быть в состоянии "установлен" или "снят", независимо от состояний других флажков. Другими словами, в группе Checkbutton можно сделать множественный выбор, в группе Radiobutton – нет.
