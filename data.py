example_data = {
    "report_header": {
        "top_header": "1 Ожирение",
        "bottom_header": "*****",
        "address": "123 Main Street",
    },
    "personal_data": {
        "patient_name": "Иванов Иван Иванович",
        "patient_age": 32,
        "patient_id": "3213123",
        "biosample_type": "Кал",
        "collection_date": "22.01.2023",
        "analysis_type": "Lorem ipsum dolor sit amet",
        "report_date": "23.01.2023",
    },
    "out_of_norm_table": [
        {"name": "Firmicutes", "amount": 29, "norm": {"lower": 10, "upper": 20}},
        {"name": "Bacteroidetes", "amount": 56, "norm": {"lower": 30, "upper": 60}},
        {"name": "Bacteroidetes", "amount": 56, "norm": {"lower": 30, "upper": 60}},
    ],
    "out_of_norm_text": "Согласно проведенному анализу наблюдаются отклонения от нормы в выше представленных бактериях. Для нормализации микробиоты кишечника следуйте рекомендациям, описанным далее в отчете",
    "pathogen": {
        "title": "Обнаружено повышенное содержание патогенных бактерии",
        "table": [
            {
                "name": "Yersinia",
                "amount": 0.90,
                "desc": "ухудшает переваривание клетчатки",
            },
            {
                "name": "Firmicutes",
                "amount": 8.20,
                "desc": "потенциально может стать одним из факторов развития рака кишечника",
            },
        ],
    },
    "probiotic": {
        "title": "Обнаружено повышенное содержание положительных бактерии",
        "table": [
            {
                "name": "Yersinia",
                "amount": 0.90,
                "desc": "потенциально может стать одним из факторов развития рака кишечника",
            },
            {
                "name": "Firmicutes",
                "amount": 8.20,
                "desc": "просто плохая, мы устали писать",
            },
        ],
    },
    "diets": [
        {
            "name": "Средиземноморская диета",
            "desc": "Средиземноморская диета характеризуется повышенным содержанием фруктов, овощей и морепродуктов.",
            "nutrition": {
                "calories": 10,
                "proteins": 32,
                "fats": 41,
                "carbohydrates": 32,
            },
            "products": ["яблоки", "оливки", "мидии", "яблоки", "оливки", "мидии"],
        },
        {
            "name": "Средиземноморская диета",
            "desc": "Средиземноморская диета характеризуется повышенным содержанием фруктов, овощей и морепродуктов.",
            "nutrition": {
                "calories": 10,
                "proteins": 32,
                "fats": 41,
                "carbohydrates": 32,
            },
            "products": ["яблоки", "оливки", "мидии", "яблоки", "оливки", "мидии"],
        },
    ],
    "products_table": [
        {
            "name": "яблоки",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "яблоки",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "яблоки",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "яблоки",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
    ],
    "additives_table": [
        {
            "name": "Клетчатка",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "Клетчатка",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "Клетчатка",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
        {
            "name": "Клетчатка",
            "amount": "200 г/день",
            "duration": "6 недель",
            "bacterias": ["Firmicutes", "Monoglobus"],
        },
    ],
    "allergens_list": ["X", "Y", "Z"],
    "age_text": "51 год – примерный возраст микробиоты. Обнаружено негативное отклонение от биологического возраста. Такой результат может указывать",
    "microbiota_age": 32,
    "main_disease": {
        "name": "A",
        "desc": "Ваша микробиота больше всего похожа на людей с заболеванием А.",
    },
    "risk_list": [
        {"name": "A", "level": "пониженный"},
        {"name": "B", "level": "повышенный"},
        {"name": "C", "level": "пониженный"},
    ],
    "conclusion": [
        {
            "text": "Кишечный микробиом пациента не характеризуется значительным разнообразием, что является основным признаком ненормального и нестабильного микробиома."
        },
        {
            "text": "Наблюдается низкая представленность «полезных» групп и низкая представленность «полезных» пробиотических штаммов."
        },
        {
            "text": "Наблюдается низкая представленность «полезных» групп и низкая представленность «полезных» пробиотических штаммов."
        },
        {
            "text": "Выявленный профиль микробиома ассоциирован с оижрением и повышенным риском развития атеросклероза, а также с развитием кишечных инфекций."
        },
    ],
}
