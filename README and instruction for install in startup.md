EN: 
To add the program to the Windows startup, 
press Win + R, then enter “shell:startup” 
and move the “OSD.exe” program shortcut to the folder that opens. 
Then restart the laptop or computer to check.

RU: 
Для установки в автозапуск Windows, 
нажмите Win + R, затем введите "shell:startup" 
и в открывшуюся папку перенесите ярлык программы "OSD.exe". 
Затем для проверки перезапустите ноутбук или компьютер. 


################## EN INFORMATION #########################
  The program displays pop‑up notifications (OSD) when the following states change:
    - Caps Lock (on/off)
    - Num Lock (on/off)
    - Input language (keyboard layout)
    - Connecting / disconnecting the laptop’s charger
  Notifications appear in the center of the screen and automatically disappear after 2 seconds.
  The design follows the style of Lenovo laptops (semi‑transparent dark background, white text, emoji icons).
  Additionally, an audio‑based CPU temperature monitoring system is implemented:
    - When the temperature exceeds 83 °C, there is one short double beep (BIOS simulation).
    - When the temperature reaches 91 °C, there is another identical signal.
    - The signal repeats only after the temperature drops below 80 °C (hysteresis).
    - The sound is played in a separate thread and does not block the interface.
  The program runs in the background, does not create windows, and has almost no impact on the processor (0–0.5%). 
  Status polling occurs every 150 ms.



################# РУ ИНФОРМАЦИЯ ###########################
  Программа показывает всплывающие уведомления (OSD) при изменении следующих состояний:
    - Caps Lock (вкл/выкл)
    - Num Lock (вкл/выкл)
    - Язык ввода (раскладка клавиатуры)
    - Подключение / отключение зарядного устройства ноутбука
  Уведомления появляются в центре экрана, автоматически исчезают через 2 секунды.  
  Оформление выполнено в стиле ноутбуков Lenovo (полупрозрачный тёмный фон, белый текст, иконки-эмодзи).
  Дополнительно реализован звуковой мониторинг температуры процессора:
    - При превышении 83 °C – один короткий двойной писк (имитация BIOS).
    - При достижении 91 °C – ещё один такой же сигнал.
    - Сигнал повторяется только после того, как температура опустится ниже 80 °C (гистерезис).
    - Звук воспроизводится в отдельном потоке, не блокирует интерфейс.
  Программа работает в фоновом режиме, не создаёт окон, почти не нагружает процессор (0–0,5%).  
  Опрос состояний происходит каждые 150 мс.
  Для работы требуется Windows и установленная библиотека psutil (для температуры).  
  Если psutil отсутствует, мониторинг температуры отключается, все остальные функции сохраняются.
    Управление: программа не имеет интерфейса, завершить можно через Диспетчер задач
