from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


from langchain_tavily import TavilySearch
from langchain_tavily.tavily_crawl import TavilyCrawlInput


class GooglePlaceSearchTool:

    def __init__(self,api_key) -> None:
        self.place_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.place_tool = GooglePlacesTool(api_wrapper=self.place_wrapper)

    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API.
        """
        return self.place_tool.run(f"top attractive places in and around {place}")

    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(
            f"what are the top 10 restaurants and eateries in and around {place}?"
        )

    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """

        return self.place_tool.run(f"Activities in and around {place}")

    def google_search_transportation(self, place: str) -> dict:
        """

        Searches for available modes of transportation in the specified place using GooglePlaces API.
        """

        return self.place_tool.run(
            f"what are the differnece modes of transfortation availble in {place}"
        )


class TavilyPlaceSearchTool:
    def __init__(self,api_key):
        self.tavily_tool = TavilySearch(topic="general", include_answers="advanced")

    def tavliy_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        result = self.tavily_tool.invoke(
            {"query": f"top attractive places in and around {place}"}
        )
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavliy_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        result = self.tavily_tool.invoke(
            {
                "query": f"what are the top 10 restaurants and eateries in and around {place}."
            }
        )
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        result = self.tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """

        result = self.tavily_tool.invoke(
            {
                "query": f"What are the different modes of transportations available in {place}"
            }
        )
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
