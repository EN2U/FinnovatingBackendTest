INSERT INTO public.establishment_establishment (id, direction,name,rating,description) VALUES
	 (1, 'Calle estibal, 54','Cines Cantones',5,'Cine de A Coruña'),
	 (2, 'Calle alambra, 76','Multicines Bergantiños',5,'Cine de A Coruña, Carballo');

INSERT INTO public.movie_movie (id, title,category,director,premiere_date,expiration_date,duration,cinema_id) VALUES
	 (1, 'Minions: El origen de Gru','Infantil','Kyle Balda','2022-05-02','2022-09-03',110,1),
	 (2, 'Minions: El origen de Gru','Infantil','Kyle Balda','2022-05-02','2022-09-03',110,2),
	 (3, 'Thor: Love and Thunder','Acción','Taika Waititi','2022-05-02','2022-09-03',120,2),
	 (4, 'Bullet Train','Suspense','David Leitch','2022-05-02','2022-09-03',120,1);