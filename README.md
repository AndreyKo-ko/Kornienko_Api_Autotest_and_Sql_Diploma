# Kornienko_Api_Autotest_and_Sql_Diploma
# Работа с базой данных
* SELECT "Couriers".login, COUNT(*) AS "deliveryCount" FROM "Couriers" JOIN "Orders" ON "Couriers".id = "Orders"."courierId" WHERE "Orders"."inDelivery" = true GROUP BY "Couriers".login;
* SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders";
# Автоматизация теста к API
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
* Клиент создает заказ.
* Проверяется, что по треку заказа можно получить данные о заказе.
## Шаги автотеста:
* Выполнить запрос на создание заказа.
* Сохранить номер трека заказа.
* Выполнить запрос на получения заказа по треку заказа.
* Проверить, что код ответа равен 200.
