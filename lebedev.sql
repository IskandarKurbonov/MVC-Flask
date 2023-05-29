-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 29 2023 г., 21:37
-- Версия сервера: 10.4.27-MariaDB
-- Версия PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `lebedev`
--

-- --------------------------------------------------------

--
-- Структура таблицы `accessory`
--

CREATE TABLE `accessory` (
  `name_of_accessory` varchar(45) NOT NULL,
  `quantity_of_accessory` int(11) DEFAULT NULL,
  `type_of_accessory` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `accessory`
--

INSERT INTO `accessory` (`name_of_accessory`, `quantity_of_accessory`, `type_of_accessory`) VALUES
('Accessory1', 214, 'Type');

-- --------------------------------------------------------

--
-- Структура таблицы `backup`
--

CREATE TABLE `backup` (
  `date_of_backup` date NOT NULL,
  `content_of_backup` varchar(255) DEFAULT NULL,
  `size_of_backup` int(11) DEFAULT NULL,
  `users_login_responsible_of_backup` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `backup`
--

INSERT INTO `backup` (`date_of_backup`, `content_of_backup`, `size_of_backup`, `users_login_responsible_of_backup`) VALUES
('2023-05-28', 'Backup', 124, 'Dmitriy');

-- --------------------------------------------------------

--
-- Структура таблицы `client`
--

CREATE TABLE `client` (
  `name_of_client` varchar(40) NOT NULL,
  `surname_of_client` varchar(45) DEFAULT NULL,
  `address_of_client` varchar(45) DEFAULT NULL,
  `number_phone_of_client` int(11) DEFAULT NULL,
  `type_of_appeals` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `client`
--

INSERT INTO `client` (`name_of_client`, `surname_of_client`, `address_of_client`, `number_phone_of_client`, `type_of_appeals`) VALUES
('Dmitriy', 'Surname', 'Address', 21421, 'Type');

-- --------------------------------------------------------

--
-- Структура таблицы `dealer`
--

CREATE TABLE `dealer` (
  `name_of_dealer` varchar(45) NOT NULL,
  `address_of_dealer` varchar(45) DEFAULT NULL,
  `type_of_services_from_dealer` varchar(45) DEFAULT NULL,
  `payment_to_the_dealer` int(11) DEFAULT NULL,
  `date_of_contract_with_dealer` date DEFAULT NULL,
  `number_of_dealer` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `dealer`
--

INSERT INTO `dealer` (`name_of_dealer`, `address_of_dealer`, `type_of_services_from_dealer`, `payment_to_the_dealer`, `date_of_contract_with_dealer`, `number_of_dealer`) VALUES
('Dmitriy', 'Arkhangelsk', 'service', 1, '2022-02-22', 142);

-- --------------------------------------------------------

--
-- Структура таблицы `delivery`
--

CREATE TABLE `delivery` (
  `name_of_courier` varchar(45) NOT NULL,
  `surname_of_courier` varchar(45) DEFAULT NULL,
  `name_of_product` varchar(45) DEFAULT NULL,
  `price_with_delivery` int(11) DEFAULT NULL,
  `from_Stock_address_of_stock` varchar(100) NOT NULL,
  `to_Client_address_of_client` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `delivery`
--

INSERT INTO `delivery` (`name_of_courier`, `surname_of_courier`, `name_of_product`, `price_with_delivery`, `from_Stock_address_of_stock`, `to_Client_address_of_client`) VALUES
('Dmitriy', 'Lebedev', 'Product', 1241, 'Stock', 'Client');

-- --------------------------------------------------------

--
-- Структура таблицы `departure`
--

CREATE TABLE `departure` (
  `type_of_service` varchar(45) NOT NULL,
  `price_of_service` varchar(45) DEFAULT NULL,
  `result` varchar(45) DEFAULT NULL,
  `status_of_departure` varchar(45) DEFAULT NULL,
  `To_Client_address_of_client` varchar(45) NOT NULL,
  `responsible` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `departure`
--

INSERT INTO `departure` (`type_of_service`, `price_of_service`, `result`, `status_of_departure`, `To_Client_address_of_client`, `responsible`) VALUES
('Type of service', '21412', 'Done', 'Wait', 'lebedev', 'Dmitriy');

-- --------------------------------------------------------

--
-- Структура таблицы `installation_and_deployment`
--

CREATE TABLE `installation_and_deployment` (
  `date_of_installation` date NOT NULL,
  `type_of_installation` varchar(250) DEFAULT NULL,
  `status_of_installation` varchar(45) DEFAULT NULL,
  `duration_time` float DEFAULT NULL,
  `result` varchar(45) DEFAULT NULL,
  `Users_login_responsible_of_installation` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `installation_and_deployment`
--

INSERT INTO `installation_and_deployment` (`date_of_installation`, `type_of_installation`, `status_of_installation`, `duration_time`, `result`, `Users_login_responsible_of_installation`) VALUES
('2022-08-28', 'Type', 'Status', 213.121, 'Result', 'Dmitriy');

-- --------------------------------------------------------

--
-- Структура таблицы `order_in_the_hall`
--

CREATE TABLE `order_in_the_hall` (
  `date_of_order` date NOT NULL,
  `price_for_technique` int(11) DEFAULT NULL,
  `quantity_of_technique` int(11) DEFAULT NULL,
  `Client_name_of_client` varchar(40) NOT NULL,
  `Technique_type_of_technique` varchar(45) NOT NULL,
  `Users_loginresponsible_for_order` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `order_in_the_hall`
--

INSERT INTO `order_in_the_hall` (`date_of_order`, `price_for_technique`, `quantity_of_technique`, `Client_name_of_client`, `Technique_type_of_technique`, `Users_loginresponsible_for_order`) VALUES
('2022-05-30', 142, 241, 'Дмитрий', 'Technique', 'Lebedev');

-- --------------------------------------------------------

--
-- Структура таблицы `purchase`
--

CREATE TABLE `purchase` (
  `name_of_product` varchar(50) NOT NULL,
  `quantity_of_product` int(11) DEFAULT NULL,
  `description_of_product` varchar(150) DEFAULT NULL,
  `factory_number` int(11) DEFAULT NULL,
  `serial_number` int(11) DEFAULT NULL,
  `purchase_amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `purchase`
--

INSERT INTO `purchase` (`name_of_product`, `quantity_of_product`, `description_of_product`, `factory_number`, `serial_number`, `purchase_amount`) VALUES
('Prod', 214, 'Product', 142, 12411, 214412);

-- --------------------------------------------------------

--
-- Структура таблицы `report_for_tax`
--

CREATE TABLE `report_for_tax` (
  `date_of_formation_report` date NOT NULL,
  `date_of_sendig_report` date DEFAULT NULL,
  `signature` varchar(45) DEFAULT NULL,
  `to_tax` varchar(45) DEFAULT NULL,
  `from_company` varchar(45) DEFAULT NULL,
  `content_of_report` varchar(255) DEFAULT NULL,
  `type_of_delivery_report` varchar(45) DEFAULT NULL,
  `Users_login_responsible_for_the_report` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `report_for_tax`
--

INSERT INTO `report_for_tax` (`date_of_formation_report`, `date_of_sendig_report`, `signature`, `to_tax`, `from_company`, `content_of_report`, `type_of_delivery_report`, `Users_login_responsible_for_the_report`) VALUES
('2022-05-05', '2023-05-05', 'Sign', 'To', 'Company', 'Content', 'Type', 'Responsible');

-- --------------------------------------------------------

--
-- Структура таблицы `service_department`
--

CREATE TABLE `service_department` (
  `address_of_service_department` varchar(45) NOT NULL,
  `quantity_stuff_in_service_department` int(11) DEFAULT NULL,
  `number_phone_of_service_department` int(11) DEFAULT NULL,
  `post_code_of_service_department` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `service_department`
--

INSERT INTO `service_department` (`address_of_service_department`, `quantity_stuff_in_service_department`, `number_phone_of_service_department`, `post_code_of_service_department`) VALUES
('Arkhangelsk', 21421, 21412, 214124);

-- --------------------------------------------------------

--
-- Структура таблицы `stock`
--

CREATE TABLE `stock` (
  `address_of_stock` varchar(100) NOT NULL,
  `quantity_of_stuff` int(11) DEFAULT NULL,
  `type_of_stock` varchar(45) DEFAULT NULL,
  `number_phone_of_stock` int(11) DEFAULT NULL,
  `Users_login_responsible_of_stock` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `stock`
--

INSERT INTO `stock` (`address_of_stock`, `quantity_of_stuff`, `type_of_stock`, `number_phone_of_stock`, `Users_login_responsible_of_stock`) VALUES
('Arkhangelsk', 214, 'Type', 21, 'Lebedev');

-- --------------------------------------------------------

--
-- Структура таблицы `technique`
--

CREATE TABLE `technique` (
  `name_of_technique` varchar(45) NOT NULL,
  `type_of_technique` varchar(45) DEFAULT NULL,
  `serial_number` int(11) DEFAULT NULL,
  `factory_number` int(11) DEFAULT NULL,
  `quantity_of_technique` int(11) DEFAULT NULL,
  `Users_login_responsible_for_the_technique` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `technique`
--

INSERT INTO `technique` (`name_of_technique`, `type_of_technique`, `serial_number`, `factory_number`, `quantity_of_technique`, `Users_login_responsible_for_the_technique`) VALUES
('Technique', 'Type2', 412421, 21412, 2141, 'Lebedev');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `login` varchar(40) NOT NULL,
  `password` varchar(24) DEFAULT NULL,
  `authentication` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`login`, `password`, `authentication`) VALUES
('Dmitriy', 'sadsad', 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `accessory`
--
ALTER TABLE `accessory`
  ADD PRIMARY KEY (`name_of_accessory`);

--
-- Индексы таблицы `backup`
--
ALTER TABLE `backup`
  ADD PRIMARY KEY (`date_of_backup`);

--
-- Индексы таблицы `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`name_of_client`);

--
-- Индексы таблицы `dealer`
--
ALTER TABLE `dealer`
  ADD PRIMARY KEY (`name_of_dealer`);

--
-- Индексы таблицы `delivery`
--
ALTER TABLE `delivery`
  ADD PRIMARY KEY (`name_of_courier`);

--
-- Индексы таблицы `departure`
--
ALTER TABLE `departure`
  ADD PRIMARY KEY (`type_of_service`);

--
-- Индексы таблицы `installation_and_deployment`
--
ALTER TABLE `installation_and_deployment`
  ADD PRIMARY KEY (`date_of_installation`);

--
-- Индексы таблицы `order_in_the_hall`
--
ALTER TABLE `order_in_the_hall`
  ADD PRIMARY KEY (`date_of_order`);

--
-- Индексы таблицы `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`name_of_product`);

--
-- Индексы таблицы `report_for_tax`
--
ALTER TABLE `report_for_tax`
  ADD PRIMARY KEY (`date_of_formation_report`);

--
-- Индексы таблицы `service_department`
--
ALTER TABLE `service_department`
  ADD PRIMARY KEY (`address_of_service_department`);

--
-- Индексы таблицы `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`address_of_stock`);

--
-- Индексы таблицы `technique`
--
ALTER TABLE `technique`
  ADD PRIMARY KEY (`name_of_technique`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`login`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
