from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel



def write_report(filename, html):
    with open(filename, 'w') as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

# whenever you create a tool, the tool has only one arguments so we use structured tool to pass more than one argument
write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Writes an HTML report to a file on disk. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema
)
