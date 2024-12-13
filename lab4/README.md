Здесь равзворачивается такой же бот, как в лабораторной 4.

### Ход работы:

1. Запускаем minikube, подключаемся к дашборду.

![](screenshot_photos/image1.png)

![](screenshot_photos/image2.png)


2. Строим образ для бота по `Dockerfile`.

![](screenshot_photos/image3.png)

![](screenshot_photos/image4.png)

3. Грузим его в minikube.

![](screenshot_photos/image5.png)

4. Строим объекты для базы данных.

![](screenshot_photos/image6.png)

![](screenshot_photos/image7.png)

5. Разворачиваем деплоймент бота (также в нем init-контейнер, выводящий сообщение об иницилизации из образа busybox).

![](screenshot_photos/image8.png)

6. Получили 2 работающих пода

![](screenshot_photos/image9.png)

7. Можем посмотреть дашборд

![](screenshot_photos/image10.png)

![](screenshot_photos/image11.png)
