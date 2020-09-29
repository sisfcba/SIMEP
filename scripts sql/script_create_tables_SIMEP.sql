CREATE TABLE `catodo` (
  `Data` datetime DEFAULT NULL,
  `Sala` int(1) DEFAULT NULL,
  `Forno` int(4) DEFAULT NULL,
  `Variavel` char(15) DEFAULT NULL,
  `Valor` varchar(4) DEFAULT NULL,
  `Usuario` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `user_federativa` (
  `Data` datetime DEFAULT NULL,
  `Nome` varchar(30) DEFAULT NULL,
  `Matricula` int(6) DEFAULT NULL,
  `Setor` varchar(10) DEFAULT NULL,
  `Turno` varchar(5) DEFAULT NULL,
  `usuario` varchar(15) NOT NULL,
  `senha` int(6) NOT NULL,
  PRIMARY KEY (`senha`)
) ENGINE=FEDERATED DEFAULT CHARSET=utf8 CONNECTION='mysql://admin:geral@10.10.11.92:3306/medicao_sf3/user_medicao'

CREATE TABLE `user_local` (
  `Data` datetime DEFAULT NULL,
  `Nome` varchar(30) DEFAULT NULL,
  `Matricula` int(6) DEFAULT NULL,
  `Setor` varchar(10) DEFAULT NULL,
  `Turno` varchar(5) DEFAULT NULL,
  `usuario` varchar(15) NOT NULL,
  `senha` int(6) NOT NULL,
  PRIMARY KEY (`senha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8