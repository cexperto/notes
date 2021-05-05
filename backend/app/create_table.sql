CREATE TABLE public.teachers
(
    id_t integer NOT NULL DEFAULT nextval('teachers_id_t_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    CONSTRAINT teachers_pkey PRIMARY KEY (id_t)
)
-- Table: public.groups

-- DROP TABLE public.groups;

CREATE TABLE public.groups
(
    id_g integer NOT NULL DEFAULT nextval('groups_id_g_seq'::regclass),
    name_g character varying COLLATE pg_catalog."default",
    fk_teacher integer,
    CONSTRAINT groups_pkey PRIMARY KEY (id_g),
    CONSTRAINT groups_teachers_fkey FOREIGN KEY (fk_teacher)
        REFERENCES public.teachers (id_t) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)


CREATE TABLE public.students
(
    id_s integer NOT NULL DEFAULT nextval('students_id_s_seq'::regclass),
    name_s character varying COLLATE pg_catalog."default",
    fk_group integer,
    CONSTRAINT students_pkey PRIMARY KEY (id_s),
    CONSTRAINT students_groups_fkey FOREIGN KEY (fk_group)
        REFERENCES public.groups (id_g) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

CREATE TABLE public.courses
(
    id_c integer NOT NULL DEFAULT nextval('courses_id_c_seq'::regclass),
    name_c character varying COLLATE pg_catalog."default",
    fk_teacher integer,
    CONSTRAINT courses_pkey PRIMARY KEY (id_c),
    CONSTRAINT courses_teachers_fkey FOREIGN KEY (fk_teacher)
        REFERENCES public.teachers (id_t) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
CREATE TABLE public.student_courses
(
    id_s_c integer NOT NULL DEFAULT nextval('student_courses_id_s_c_seq'::regclass),
    fk_student integer,
    fk_course integer,
    CONSTRAINT student_courses_pkey PRIMARY KEY (id_s_c),
    CONSTRAINT courses_s_fkey FOREIGN KEY (fk_course)
        REFERENCES public.courses (id_c) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT student_c_fkey FOREIGN KEY (fk_student)
        REFERENCES public.students (id_s) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
CREATE TABLE public.notes
(
    id_n integer NOT NULL DEFAULT nextval('notes_id_n_seq'::regclass),
    period1 numeric,
    period2 numeric,
    period3 numeric,
    fk_student integer,
    fk_course integer,
    CONSTRAINT notes_pkey PRIMARY KEY (id_n),
    CONSTRAINT notes_courses_fkey FOREIGN KEY (fk_course)
        REFERENCES public.courses (id_c) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
