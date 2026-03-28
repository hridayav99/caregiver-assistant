import requests
import xml.etree.ElementTree as et
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("MedlinePlus Health Information")

@mcp.tool()
def get_condition_info(condition: str) -> str:
    """
    Fetches health information about a medical condition from NIH MedlinePlus.
    Use this to get caregiver guidance for a specific condition like diabetes, dementia, or cancer.
    
    Args:
        condition: The medical condition to search for e.g. diabetes, dementia
    """
    url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term={condition}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        root = et.fromstring(response.content)
        
        results = []
        for doc in root.findall('.//document'):
            title = doc.find('.//content[@name="title"]')
            summary = doc.find('.//content[@name="FullSummary"]')
            
            if title is not None and summary is not None:
                results.append(f"Topic: {title.text}\n\nInformation: {summary.text}")
        
        if results:
            return "\n\n---\n\n".join(results[:2])
        else:
            return f"No information found for condition: {condition}"
            
    except Exception as e:
        return f"Error fetching information: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")