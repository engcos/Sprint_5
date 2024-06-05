class Locator:
    ACCOUNT_BUTTON = "//a[contains(@href, '/account')]"
    REGISTRATION_BUTTON = "//a[contains(@href, '/register')]"
    NAME_INPUT = "(.//label[text()='Имя']/following::input)[1]"
    EMAIL_INPUT = "(.//label[text()='Email']/following::input)[1]"
    PASS_INPUT = "(.//label[text()='Пароль']/following::input)[1]"
    REGISTRATION_COMMIT_BUTTON = "//button[contains(text(), 'Зарегистрироваться')]"
    LOGIN_BUTTON = "//button[contains(text(), 'Войти')]"
    CREATE_ORDER_BUTTON = "//button[contains(text(), 'Оформить заказ')]"
    ERROR_LABEL = "p.input__error"
    ENTER_ACCOUNT = "//button[contains(text(), 'Войти в аккаунт')]"
    ENTER_ACCOUNT_BUTTON = "//a[contains(@href, '/login')]"
    FORGOT_PASSWORD_BUTTON = "//a[contains(@href, '/forgot-password')]"
    EXIT_BUTTON = "//button[contains(text(), 'Выход')]"
    CONSTRUCTOR_BUTTON = "//a[contains(@href, '/')]"
    STELLAR_BURGET_BUTTON = ["//div[contains(@class, 'AppHeader_header__logo__2D0X2')]", "//a[contains(@href, '/')]"]
    SAUCESS_BUTTON = "//span[contains(text(), 'Соусы')]"
    FILLINGS_BUTTON = "//span[contains(text(), 'Начинки')]"
    ROLLS_BUTTON = "//span[contains(text(), 'Булки')]"
    PARENT_DIV_OF_SAUCESS_BUTTON = ["//div[contains(@class, 'tab_tab_type_current__2BEPc')]", "//span[contains(text(), 'Соусы')]"]
    PARENT_DIV_OF_FILLINGS_BUTTON = ["//div[contains(@class, 'tab_tab_type_current__2BEPc')]", "//span[contains(text(), 'Начинки')]"]
    PARENT_DIV_OF_ROLLS_BUTTON = ["//div[contains(@class, 'tab_tab_type_current__2BEPc')]", "//span[contains(text(), 'Булки')]"]
