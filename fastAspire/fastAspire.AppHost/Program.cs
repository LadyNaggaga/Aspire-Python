using Microsoft.Extensions.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

#pragma warning disable ASPIREHOSTINGPYTHON001
var backend = builder.AddPythonApp("backend", "../backend", "main.py")
    .WithHttpEndpoint(env: "PORT")
    .WithExternalHttpEndpoints()
    .WithOtlpExporter();
#pragma warning restore ASPIREHOSTINGPYTHON001

var frontend = builder.AddNpmApp("src", "../frontend", "index.html")
    .WithHttpEndpoint(port: 5174, env: "PORT")
    .WithReference(backend);

builder.Build().Run();
