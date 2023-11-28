-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2023 a las 21:51:11
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_ordenes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_ordenes`
--

CREATE TABLE `categoria_ordenes` (
  `categoria` int(11) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria_ordenes`
--

INSERT INTO `categoria_ordenes` (`categoria`, `descripcion`) VALUES
(1, 'HARDWARE'),
(2, 'SOFTWARE'),
(3, 'RED');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id_dep` int(11) NOT NULL,
  `departamento` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id_dep`, `departamento`) VALUES
(1, 'JEFATURA'),
(2, 'TIC'),
(3, 'TECNICOS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `Id_emp` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `run` varchar(13) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `foto` blob DEFAULT NULL,
  `fecha_nacimiento` date NOT NULL,
  `id_rol` int(11) NOT NULL,
  `id_dep` int(11) DEFAULT NULL,
  `id_jefe` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`Id_emp`, `id`, `run`, `nombre`, `foto`, `fecha_nacimiento`, `id_rol`, `id_dep`, `id_jefe`) VALUES
(1, 1, '0.000.000-0', 'admin', NULL, '1999-12-17', 1, 1, 1),
(2, 3, '1.111.111-1', 'usuario', NULL, '1999-12-17', 2, 2, 1),
(3, 2, '2.222.222-2', 'tecnico', NULL, '2023-12-31', 3, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_ordenes`
--

CREATE TABLE `estado_ordenes` (
  `estado` int(11) NOT NULL,
  `descripcion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado_ordenes`
--

INSERT INTO `estado_ordenes` (`estado`, `descripcion`) VALUES
(1, 'INGRESADO'),
(2, 'EN CURSO'),
(3, 'CERRADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes`
--

CREATE TABLE `ordenes` (
  `id_orden` int(11) NOT NULL,
  `categoria` int(11) NOT NULL,
  `detalle` varchar(5000) NOT NULL,
  `fecha_emision` datetime NOT NULL,
  `id_dep` int(11) NOT NULL,
  `run_emp` varchar(13) NOT NULL,
  `estado` int(11) NOT NULL,
  `run_tecnico` varchar(13) DEFAULT NULL,
  `fecha_termino` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ordenes`
--

INSERT INTO `ordenes` (`id_orden`, `categoria`, `detalle`, `fecha_emision`, `id_dep`, `run_emp`, `estado`, `run_tecnico`, `fecha_termino`) VALUES
(1, 1, 'ORDEN DE PRUEBA HARDWARE', '2023-11-18 04:04:46', 2, '00.000.000.00', 1, NULL, NULL),
(2, 2, 'ORDEN PRUEBA SOFTWARE', '2023-11-18 04:05:00', 2, '11.111.111.11', 2, '2.222.222-2', NULL),
(3, 3, 'ORDEN PRUEBA RED', '2023-11-18 04:05:18', 3, '22.222.222.22', 3, '3.333.333-2', NULL),
(4, 2, 'mi programa no funciona ayuda', '2023-11-20 17:16:37', 2, '20.180.895-2', 3, '2.222.222-2', '2023-11-20 17:21:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `descripcion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `descripcion`) VALUES
(1, 'ADMIN'),
(2, 'USUARIO'),
(3, 'TECNICO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Id` int(11) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id`, `correo`, `password`, `id_rol`) VALUES
(1, 'admin@gmail.com', '1234', 1),
(2, 'usuario@gmail.com', '1234', 2),
(3, 'tecnico@gmail.com', '1234', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria_ordenes`
--
ALTER TABLE `categoria_ordenes`
  ADD PRIMARY KEY (`categoria`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id_dep`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`Id_emp`),
  ADD KEY `id` (`id`),
  ADD KEY `id_dep` (`id_dep`),
  ADD KEY `id_rol` (`id_rol`),
  ADD KEY `id_jefe` (`id_jefe`);

--
-- Indices de la tabla `estado_ordenes`
--
ALTER TABLE `estado_ordenes`
  ADD PRIMARY KEY (`estado`);

--
-- Indices de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  ADD PRIMARY KEY (`id_orden`),
  ADD KEY `categoria` (`categoria`),
  ADD KEY `id_dep` (`id_dep`),
  ADD KEY `estado` (`estado`),
  ADD KEY `run_emp` (`run_emp`),
  ADD KEY `run_tecnico` (`run_tecnico`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `correo` (`correo`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id_dep` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `Id_emp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  MODIFY `id_orden` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_2` FOREIGN KEY (`id`) REFERENCES `usuarios` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `empleados_ibfk_3` FOREIGN KEY (`id_dep`) REFERENCES `departamentos` (`id_dep`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `empleados_ibfk_5` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `empleados_ibfk_6` FOREIGN KEY (`id_jefe`) REFERENCES `empleados` (`Id_emp`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `ordenes`
--
ALTER TABLE `ordenes`
  ADD CONSTRAINT `ordenes_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categoria_ordenes` (`categoria`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ordenes_ibfk_2` FOREIGN KEY (`estado`) REFERENCES `estado_ordenes` (`estado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ordenes_ibfk_3` FOREIGN KEY (`id_dep`) REFERENCES `departamentos` (`id_dep`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
