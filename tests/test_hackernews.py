import re, unittest
from operator import itemgetter

from appium.webdriver.common.mobileby import MobileBy as By

from helpers.driver import DriverProvider
from helpers.logger import LoggerProvider

logger = LoggerProvider.get_logger(__name__)


class HackerNews(unittest.TestCase):
    """
    Teste para App Materialistic, um cliente Hacker News, com código
    disponível em https://github.com/hidroh/materialistic.
    Decidi usar esse app pela possibilidade de criar o apk correspondente
    a partir do seu próprio código-fonte, o mais atualizado da lista disponível
    em https://github.com/cheeaun/awesome-hacker-news#android.

    O teste abaixo verifica se há algum artigo relacionado a Open Source entre
    os 10 primeiros da lista Top Stories, apresentada assim que o App é aberto.
    Como são mostrados cinco artigos no primeiro fold da tela, foi necessário
    fazer um swipe up, exibindo mais artigos e acrescentando-os numa lista, que
    conterá os 10 primeiros títulos. Depois verificamos se o título contém as
    palavras relacionadas.

    Params
        - stories_titles: X-path da lista de títulos de artigos

    Curiosidade:
        O App tem Activities diferentes:
            - LauncherActivity: inicia o app, como uma SplashScreen;
            - ListActivity: responsável pela carga e apresentação dos artigos
        Para poder iniciar o App no Emulador, precisamos indicar duas
        capabilities:
            - appWaitPackage: package da Activity a esperar apresentação
            - appWaitActivity: Activity a apresentar após inicialização.
        Há uma terceira capability, appWaitDuration, que é o tempo que devemos
        esperar até que a Activity indicada na capability appWaitActivity seja
        apresentada, e assim possamos iniciar o teste. Não a usei, pois seu
        valor padrão é de 20000ms, tempo suficiente para o start do App.
    """

    stories_titles = (By.XPATH, "//*[contains(@resource-id,'title')]")

    def setUp(self) -> None:
        self.driver = DriverProvider.get(self.__class__.__name__.lower())

    def tearDown(self) -> None:
        if self.driver != None:
            logger.debug("Disposing Driver...")
            self.driver.quit()

    def test_there_is_an_article_about_opensource_software_on_top10(self):
        width, height = itemgetter("width", "height")(self.driver.get_window_size())
        swipe_start = (width // 2, height * 0.9)
        swipe_end = (width // 2, height * 0.2)

        titles = [
            title.text for title in self.driver.find_elements(*self.stories_titles)
        ]

        while len(titles) < 10:
            self.driver.swipe(*swipe_start, *swipe_end, duration=700)
            titles.extend(
                [
                    title.text
                    for title in self.driver.find_elements(*self.stories_titles)
                    if title.text not in titles
                ]
            )

        self.assertFalse(len(titles) == 0, "Failed to get stories")

        titles_about_opensource = list(
            filter(
                lambda title: re.compile(r"open(-| )*source").search(title) is not None,
                titles[:10],
            )
        )
        self.assertGreater(len(titles_about_opensource), 0)


if __name__ == "__main__":
    unittest.main()
