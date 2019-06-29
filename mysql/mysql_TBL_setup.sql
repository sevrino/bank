CREATE SCHEMA bank;
CREATE TABLE `bank`.`member` (
  `id` INT UNSIGNED NOT NULL,
  `usrbal` INT UNSIGNED NOT NULL,
  `usruse` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `usrbal`, `usruse`));
INSERT INTO bank.member (id, usrbal, usruse) VALUES (10101, 0, 0);
INSERT INTO bank.member (id, usrbal, usruse) VALUES (99999, 0, 0);
INSERT INTO bank.member (id, usrbal, usruse) VALUES (101, 0, 0);
SELECT * FROM bank.member;
